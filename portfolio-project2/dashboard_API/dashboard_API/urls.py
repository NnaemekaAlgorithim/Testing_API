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

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL pattern for listing and creating a team member
    path('teams/', views.TeamListView.as_view(), name='team-list'),
    # URL pattern for retrieving, updating, and deleting a team member
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team-detail'),
    # URL pattern for listing and creating Invoices
    path('invoices/', views.InvoiceListView.as_view(), name='invoice-list'),
    # URL pattern for retrieving, updating, and deleting an Invoice
    path('invoices/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    # URL pattern for listing and creating Customer Contacts
    path('customer-contacts/', views.CustomerContactsListView.as_view(), name='customer-contacts-list'),
    # URL pattern for retrieving, updating, and deleting a Customer Contact
    path('customer-contacts/<int:pk>/', views.CustomerContactsDetailView.as_view(), name='customer-contacts-detail'),
    # URL pattern for listing and creating a transaction
    path('transactions/', views.TransactionListView.as_view(), name='transaction-list'),
    # URL pattern for retrieving, updating, and deleting a transaction
    path('transactions/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-detail'),
    # URL pattern for listing and creating a barchart
    path('BarData/', views.BarDataListView.as_view(), name='BarData'),
    # URL pattern for retrieving, updating, and deleting a barchart data
    path('BarData/<int:pk>/', views.BarDataDetailView.as_view(), name='BarData-detail'),
    # URL pattern for listing and creating a piechart data
    path('PieData/', views.PieDataListView.as_view(), name='PieData'),
    # URL pattern for retrieving, updating, and deleting a piechart data
    path('PieData/<int:pk>/', views.PieDataDetailView.as_view(), name='PieData-detail'),
    # URL pattern for listing and creating a line chart data
    path('LineData/', views.LineDataListView.as_view(), name='LineData'),
    # URL pattern for retrieving, updating, and deleting a line chart data
    path('LineData/<int:pk>/', views.LineDataDetailView.as_view(), name='LineData-detail'),
]
