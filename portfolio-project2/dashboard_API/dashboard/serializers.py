from rest_framework import serializers
from .models import Team
from models_customersContacs import CustomerContact
from models_invoice import Invoice

class TeamSerializer(serializers.ModelSerializer):
    """
    A generic serializer that can be used for multiple models.

    Attributes:
        model (Model): The model class to be serialized.

    Meta:
        model (Model): The model class to be set dynamically.
        fields (str or tuple): The fields to include in the serialized representation.

    Example Usage:
        To use this serializer, set the `model` attribute before serializing data.
        serializer = GenericModelSerializer(model=YourModel, fields='__all__')
    """
    class Meta:
        model = Team  # The model will be set dynamically
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    """
    A generic serializer that can be used for multiple models.

    Attributes:
        model (Model): The model class to be serialized.

    Meta:
        model (Model): The model class to be set dynamically.
        fields (str or tuple): The fields to include in the serialized representation.

    Example Usage:
        To use this serializer, set the `model` attribute before serializing data.
        serializer = GenericModelSerializer(model=YourModel, fields='__all__')
    """
    class Meta:
        model = CustomerContact  # The model will be set dynamically
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    """
    A generic serializer that can be used for multiple models.

    Attributes:
        model (Model): The model class to be serialized.

    Meta:
        model (Model): The model class to be set dynamically.
        fields (str or tuple): The fields to include in the serialized representation.

    Example Usage:
        To use this serializer, set the `model` attribute before serializing data.
        serializer = GenericModelSerializer(model=YourModel, fields='__all__')
    """
    class Meta:
        model = Invoice  # The model will be set dynamically
        fields = '__all__'
