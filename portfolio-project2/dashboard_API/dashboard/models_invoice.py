from django.db import models


class Invoice(models.Model):
    """
    Represents an invoice.

    Attributes:
        id (AutoField): The unique identifier for the invoice.
        name (CharField): The full name associated with the invoice.
        email (EmailField): The email address associated with the invoice.
        cost (DecimalField): The cost of the invoice.
        phone (CharField): The phone number associated with the invoice.
        date (DateField): The date of the invoice.

    Methods:
        __str__(): Returns the name associated with the invoice.

    Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
    """

    id = models.AutoField(
        primary_key=True,
        help_text="The unique identifier for the invoice."
    )
    name = models.CharField(
        max_length=255,
        help_text="The full name associated with the invoice."
    )
    email = models.EmailField(
        help_text="The email address associated with the invoice."
    )
    cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="The cost of the invoice."
    )
    phone = models.CharField(
        max_length=20,
        help_text="The phone number associated with the invoice."
    )
    date = models.DateField(
        help_text="The date of the invoice."
    )

    def __str__(self):
        """
        Returns the name associated with the invoice.

        Returns:
            str: The name associated with the invoice.
        """
        return self.name

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"
