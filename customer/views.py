from django.contrib import messages
from django.contrib.messages.context_processors import messages
from django.core.checks.security.base import check_ssl_redirect
from django.shortcuts import render, redirect

from customer.models import Customer
from customer.forms import CustomerModelForm


# Create your views here.

def customers(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request,'customer/customer_list.html',context)

def add_customer(request):
    form=CustomerModelForm()
    if request.method=='POST':
        form=CustomerModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers')
    context={
        'form':form
    }
    return render(request, 'customer/add_customer.html', context)


def delete_customer(request,id):
    customer = Customer.objects.get(id=id)
    if customer:
        customer.delete()
        return redirect('customers')
        # messages.add_message(
        #     request,
        #     messages.SUCCESS,
        #     'Successfully deleted customer'

    return redirect('customers')