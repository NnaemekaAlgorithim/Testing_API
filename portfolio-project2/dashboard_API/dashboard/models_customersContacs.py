from django.db import models


class CustomerContact(models.Model):
    """
    Represents a customer contact.

    Attributes:
        id (AutoField): The unique identifier for the customer contact.
        name (CharField): The full name of the customer contact.
        email (EmailField): The email address of the customer contact.
        age (PositiveIntegerField): The age of the customer contact.
        phone (CharField): The phone number of the customer contact.
        access (CharField): The level of access granted to the customer contact (e.g., 'admin', 'manager', 'user').

    Methods:
        __str__(): Returns the name of the customer contact.

    Meta:
        verbose_name = "Customer Contact"
        verbose_name_plural = "Customer Contacts"
    """

    id = models.AutoField(
        primary_key=True,
        help_text="The unique identifier for the customer contact."
    )
    name = models.CharField(
        max_length=255,
        help_text="The full name of the customer contact."
    )
    email = models.EmailField(
        unique=True,
        help_text="The email address of the customer contact."
    )
    age = models.PositiveIntegerField(
        help_text="The age of the customer contact."
    )
    phone = models.CharField(
        max_length=20,
        help_text="The phone number of the customer contact."
    )
    access = models.CharField(
        max_length=20,
        choices=[('admin', 'Admin'), ('user', 'User'), ('manager', 'Manager')],
        default='user',
        help_text="The level of access granted to the customer contact (e.g., 'admin', 'manager', 'user')."
    )

    def __str__(self):
        """
        Returns the name of the customer contact.

        Returns:
            str: The name of the customer contact.
        """
        return self.name

    class Meta:
        verbose_name = "Customer Contact"
        verbose_name_plural = "Customer Contacts"
