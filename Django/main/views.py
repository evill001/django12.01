from django.shortcuts import render, redirect
from django.views.generic import DeleteView, UpdateView

from .models import *
from .forms import *

def Index(request):
    prod = Products.objects.all()
    return render(request, 'main/index.html', {'prod': prod})


def Clients(request):
    clients = Customers.objects.all()
    return render(request, 'main/clients.html', {'clients':clients})

def Order(request):
    orders = Orders.objects.all()
    return render(request, 'main/orders.html', {'orders':orders})

def AddProduct(request):
    error = ''
    if request.method == "POST":
        form = AddProdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была неверной"

    form = AddProdForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/addProd.html', context)
    
def AddOrder(request):
    error = ''
    if request.method == "POST":
        form = AddOrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
        else:
            error = "Форма была неверной"

    form = AddOrdersForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/addOrders.html', context)


class ProductDelete(DeleteView):
    model = Products
    success_url = "/"
    template_name = "main/delete.html"

class ProductUpdate(UpdateView):
    model = Products
    success_url = "/"
    template_name = "main/addProd.html"
    form_class = AddProdForm