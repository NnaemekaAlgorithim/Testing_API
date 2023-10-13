from rest_framework import generics
from .models import Team, CustomerContact, Invoice, Transactions, BarData, PieData, LineData
from .serializers import TeamSerializer, InvoiceSerializer, ContactsSerializer, TransactionSerializer, BarDataSerializer, PieDataSerializer, LineDataSerializer

class TeamListView(generics.ListCreateAPIView):
    """
    View for listing and creating Team members.

    Attributes:
        queryset (QuerySet): The queryset containing Team members.
        serializer_class (Serializer): The serializer class to use for Team members.

    Example Usage:
        To list Team members, make a GET request to this view.
        To create a new Team member, make a POST request with the required data.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer  # Use the GenericModelSerializer

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a Team member.

    Attributes:
        queryset (QuerySet): The queryset containing Team members.
        serializer_class (Serializer): The serializer class to use for Team members.

    Example Usage:
        To retrieve a Team member, make a GET request to this view with the Team's ID.
        To update a Team member, make a PUT or PATCH request with the updated data.
        To delete a Team member, make a DELETE request with the Team's ID.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer  # Use the GenericModelSerializer




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




class CustomerContactsListView(generics.ListCreateAPIView):
    """
    View for listing and creating Customer Contacts.

    Attributes:
        queryset (QuerySet): The queryset containing Customer Contacts.
        serializer_class (Serializer): The serializer class to use for Customer Contacts.

    Example Usage:
        To list Customer Contacts, make a GET request to this view.
        To create a new Customer Contact, make a POST request with the required data.
    """
    queryset = CustomerContact.objects.all()
    serializer_class = ContactsSerializer  # Use the GenericModelSerializer

class CustomerContactsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a Customer Contact.

    Attributes:
        queryset (QuerySet): The queryset containing Customer Contacts.
        serializer_class (Serializer): The serializer class to use for Customer Contacts.

    Example Usage:
        To retrieve a Customer Contact, make a GET request to this view with the Customer Contact's ID.
        To update a Customer Contact, make a PUT or PATCH request with the updated data.
        To delete a Customer Contact, make a DELETE request with the Customer Contact's ID.
    """
    queryset = CustomerContact.objects.all()
    serializer_class = ContactsSerializer  # Use the GenericModelSerializer




class TransactionListView(generics.ListCreateAPIView):
    """
    View for listing and creating Transactions.

    Attributes:
        queryset (QuerySet): The queryset containing Transactions.
        serializer_class (Serializer): The serializer class to use for Transactions.

    Example Usage:
        To list Transactions, make a GET request to this view.
        To create a new Transaction, make a POST request with the required data.
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer  # Use the GenericModelSerializer

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a Transaction.

    Attributes:
        queryset (QuerySet): The queryset containing Transactions.
        serializer_class (Serializer): The serializer class to use for Transactions.
    
    Example Usage:
        To retrieve a Transaction, make a GET request to this view with the Transaction's ID.
        To update a Transaction, make a PUT or PATCH request with the updated data.
        To delete a Transaction, make a DELETE request with the Transaction's ID.
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer  # Use the GenericModelSerializer




class BarDataListView(generics.ListCreateAPIView):
    """
    View for listing and creating BarData.

    Attributes:
        queryset (QuerySet): The queryset containing BarData.
        serializer_class (Serializer): The serializer class to use for BarData.

    Example Usage:
        To list BarData, make a GET request to this view.
        To create a new BarData, make a POST request with the required data.
    """
    queryset = BarData.objects.all()
    serializer_class = BarDataSerializer  # Use the GenericModelSerializer

class BarDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting BarData.

    Attributes:
        queryset (QuerySet): The queryset containing BarData.
        serializer_class (Serializer): The serializer class to use for BarData.
    
    Example Usage:
        To retrieve BarData, make a GET request to this view with the BarData's ID.
        To update BarData, make a PUT or PATCH request with the updated data.
        To delete BarData, make a DELETE request with the BarData's ID.
    """
    queryset = BarData.objects.all()
    serializer_class = BarDataSerializer  # Use the GenericModelSerializer




class PieDataListView(generics.ListCreateAPIView):
    """
    View for listing and creating PieData.

    Attributes:
        Query set (QuerySet): The queryset containing PieData.
        serializer_class (Serializer): The serializer class to use for PieData.

    Example Usage:
        To list PieData, make a GET request to this view.
        To create a new PieData, make a POST request with the required data.
    """
    queryset = PieData.objects.all()
    serializer_class = PieDataSerializer  # Use the GenericModelSerializer

class PieDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting PieData.

    Attributes:
        Query set (QuerySet): The queryset containing PieData.
        serializer_class (Serializer): The serializer class to use for PieData.
    
    Example Usage:
        To list PieData, make a GET request to this view.
        To create a new PieData, make a POST request with the required data.
    """
    queryset = PieData.objects.all()
    serializer_class = PieDataSerializer  # Use the GenericModelSerializer



class LineDataListView(generics.ListCreateAPIView):
    """
    View for listing and creating LineData.

    Attributes:
        Query set (QuerySet): The queryset containing LineData.
        serializer_class (Serializer): The serializer class to use for LineData.

    Example Usage:
        To list LineData, make a GET request to this view.
        To create a new LineData, make a POST request with the required data.
    """
    queryset = LineData.objects.all()
    serializer_class = LineDataSerializer  # Use the GenericModelSerializer

class LineDataDetailView(generics.RetrieveUpdateDestroyAPIView):
        """
        View for retrieving, updating, and deleting LineData.

        Attributes:
            Query set (QuerySet): The queryset containing LineData.
            serializer_class (Serializer): The serializer class to use for LineData.
        
        Example Usage:
            To list LineData, make a GET request to this view.
            To create a new LineData, make a POST request with the required data.
        """
        queryset = LineData.objects.all()
        serializer_class = LineDataSerializer  # Use the GenericModelSerializer
