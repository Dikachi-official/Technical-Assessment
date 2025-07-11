from django.contrib import admin

# CUSTOM MODELS
from api import models as api_models

# Register your models here.
admin.site.register(api_models.Customer)
admin.site.register(api_models.Invoice)
admin.site.register(api_models.InvoiceItem)
