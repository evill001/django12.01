from django.forms import ModelForm

from .models import *

class AddProdForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

class AddCustomersForm(ModelForm):
    class Meta:
        model = Customers
        fields = "__all__"

class AddOrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = "__all__"