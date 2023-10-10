from django.db import models

# Create your models here.
class Team(models.Model):
    """
    Represents a user in the system.

    Attributes:
        id (AutoField): The unique identifier for the user.
        name (CharField): The full name of the user.
        email (EmailField): The email address of the user.
        age (PositiveIntegerField): The age of the user.
        phone (CharField): The phone number of the user.
        access (CharField): The level of access granted to the user (e.g., 'admin', 'manager', 'user').
    """

    name = models.CharField(
        max_length=255,
        help_text="The full name of the Team member."
    )
    email = models.EmailField(
        unique=True,
        help_text="The email address of the Team member."
    )
    age = models.PositiveIntegerField(
        help_text="The age of the Team member."
    )
    phone = models.CharField(
        max_length=20,
        help_text="The phone number of the Team member."
    )
    access = models.CharField(
        max_length=20,
        choices=[('admin', 'Admin'), ('user', 'User'), ('manager', 'Manager')],
        default='user',
        help_text="The level of access granted to the user (e.g., 'admin', 'manager', 'user')."
    )

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name
