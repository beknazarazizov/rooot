from django.http import HttpResponse
from django.shortcuts import render, redirect

from app.forms import ProductForm, ProductForm
from app.models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'app/index.html',context)

def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    atributes = Product.objects.all()
    context = {'product': product,
               'atributes': atributes
               }

    return render(request,'app/product-details.html',context)

def add_product(request):
    form=ProductForm()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        name= request.POST['name']
        descriptions=request.POST['descriptions']
        price=request.POST['price']
        reting=request.POST['reting']
        discount=request.POST['discount']
        quantity=request.POST['quantity']
        product=Product(name=name,descriptions=descriptions,price=price,reting=reting,discount=discount,quantity=quantity)
        if form.is_valid():
            product.save()
            return redirect('index')

    else:
        form=ProductForm()
    context={
        'form' : form
    }
    return render(request,'app/add_product.html',context)

# def add_product(request):
#     form = ProductModelForm()
#     if request.method =='POST':
#         form = ProductModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     context = {
#         'form' : form
#     }
#     return render(request,'app/add_product.html',context)