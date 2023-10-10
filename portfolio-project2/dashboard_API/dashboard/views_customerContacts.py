from rest_framework import generics
from .models_customersContacs import CustomerContact
from .serializers import ContactsSerializer

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
