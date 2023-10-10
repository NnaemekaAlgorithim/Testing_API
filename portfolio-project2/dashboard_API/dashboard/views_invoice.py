from rest_framework import generics
from .models_invoice import Invoice
from .serializers import InvoiceSerializer

class InvoiceListView(generics.ListCreateAPIView):
    """
    View for listing and creating Invoices.

    Attributes:
        queryset (QuerySet): The queryset containing Invoices.
        serializer_class (Serializer): The serializer class to use for Invoices.

    Example Usage:
        To list Invoices, make a GET request to this view.
        To create a new Invoice, make a POST request with the required data.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer  # Use the GenericModelSerializer

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting an Invoice.

    Attributes:
        queryset (QuerySet): The queryset containing Invoices.
        serializer_class (Serializer): The serializer class to use for Invoices.

    Example Usage:
        To retrieve an Invoice, make a GET request to this view with the Invoice's ID.
        To update an Invoice, make a PUT or PATCH request with the updated data.
        To delete an Invoice, make a DELETE request with the Invoice's ID.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer  # Use the GenericModelSerializer
