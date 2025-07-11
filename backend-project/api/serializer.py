from rest_framework import serializers

# CUSTOM IMPORT
from api import models as api_models



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.Customer
        fields = '_all_'



class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = api_models.InvoiceItem
        fields = ['id', 'description', 'quantity', 'unit_price', 'total']
        read_only_fields = ['total']
        
        
        
class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True) # Multiple existing items per invoice
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = api_models.Invoice
        fields = ['id', 'customer', 'issue_date', 'due_date', 'status', 'created_at', 'items', 'total_amount']
        read_only_fields = ['created_at', 'total_amount']

    # Compute total amount
    def get_total_amount(self, obj):
        return obj.total_amount()

    # Issued date must not exceed due date
    def validate(self, data):
        if data['due_date'] < data['issue_date']:
            raise serializers.ValidationError("Due date must be after or equal to issue date.")
        return data

    # To confirm that an item exists
    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Invoice must have at least one line item.")
        return value

    # To crreate invoice and its respective item
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        invoice = api_models.Invoice.objects.create(**validated_data)
        for item_data in items_data:
            api_models.InvoiceItem.objects.create(invoice=invoice, **item_data)
        return invoice

