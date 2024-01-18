from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index, name='home'),
    path('add-product', AddProduct, name="AddProduct"),
    path('<int:pk>/delete,', ProductDelete.as_view(), name="deleteProd"),
    path('<int:pk>/update,', ProductUpdate.as_view(), name="updateProd"),
    path('customers', Clients, name="customers"),
    path('orders', Order, name="orders"),
    path('add-orders', AddOrder, name="AddOrder"),
]
