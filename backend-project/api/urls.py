from django.urls import path
from api import views as api_views


urlpatterns = [
    # Customers
    path('customers/', api_views.CustomerListCreateView.as_view()),

    # Invoices
    path('invoices/', api_views.InvoiceListCreateView.as_view()),
    path('invoices/<int:pk>/', api_views.InvoiceDetailView.as_view()),
    path('invoices/<int:pk>/status/', api_views.InvoiceStatusUpdateView.as_view()),
]