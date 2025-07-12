from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer, Invoice
from .serializer import CustomerSerializer, InvoiceSerializer, InvoiceStatusSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Create your views here.

### CUSTOMER VIEW
# POST-customers and GET-customers
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    
    
### INVOICE VIEW 
# POST-invoices and GET-invoices
class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer



# GET /invoices/<id>/
class InvoiceDetailView(generics.RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer



# PATCH /invoices/<id>/ – Update only the status field
class InvoiceStatusUpdateView(generics.UpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceStatusSerializer



