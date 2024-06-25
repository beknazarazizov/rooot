from django.urls import path

from customer.views import customers,add_customer,delete_customer

urlpatterns = [
    path('customers_list/',customers,name='customers'),
    path('add_customers/',add_customer,name='add_customer'),
    path('customer/<int:id>delete',delete_customer,name='delete'),
]