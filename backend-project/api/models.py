from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


# Create your models here.

### CUSTOMER MODEL
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
    
### INVOICE MODEL
class Invoice(models.Model):
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    ]
    
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    issue_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def total_amount(self):
        return sum(item.total for item in self.items.all())
    
    def __str__(self):
        return '{} - {}'.format(self.id, self.status)



### INVOICE ITEM MODEL
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=50, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    total = models.DecimalField(max_digits=50, decimal_places=2, editable=False)

    class Meta:
        verbose_name_plural = "Invoice-Items"
    
    # save method get for total price
    def save(self, *args, **kwargs):
        self.total = self.quantity * self.unit_price
        super().save(*args, **kwargs)
