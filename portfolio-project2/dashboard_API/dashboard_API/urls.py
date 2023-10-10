"""
URL configuration for dashboard_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard import views
from dashboard import views_customerContacts
from dashboard import views_invoice

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teams/', views.TeamListView.as_view(), name='team-list'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team-detail'),
    # URL pattern for listing and creating Invoices
    path('invoices/', views_invoice.InvoiceListView.as_view(), name='invoice-list'),
    # URL pattern for retrieving, updating, and deleting an Invoice
    path('invoices/<int:pk>/', views_invoice.InvoiceDetailView.as_view(), name='invoice-detail'),
    # URL pattern for listing and creating Customer Contacts
    path('customer-contacts/', views_customerContacts.CustomerContactsListView.as_view(), name='customer-contacts-list'),
    # URL pattern for retrieving, updating, and deleting a Customer Contact
    path('customer-contacts/<int:pk>/', views_customerContacts.CustomerContactsDetailView.as_view(), name='customer-contacts-detail'),
]
