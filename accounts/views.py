from math import prod
from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from django.http import HttpResponse
from accounts.decorators import allowed_user
from .models import *
from .forms import *
from .filters import OrderFilter
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def products(request):
    prod = product.objects.all()
    return render(request,'products.html',{'prod':prod})

@login_required(login_url='login')
def customers(request,link):
    cust = customer.objects.get(id=link)
    orders = cust.order_set.all()
    total_orders = orders.count()
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs
    data= {
        'customer':cust,
        'order':orders,
        'total_orders':total_orders,
        'order_filter':order_filter,
    }
    return render(request, 'customer.html',data)
    
@login_required(login_url='login')
def createOrder(request,link):
    OrderFormSet = inlineformset_factory(customer, order, fields=('product','status',))
    orders = customer.objects.get(id=link)
    formset = OrderFormSet(queryset=order.objects.none() ,instance=orders)
    
    #form = orderForm(initial={'customer':orders})
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=orders)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    return render(request,'create_form.html',{'formset':formset})

@login_required(login_url='login')
def updateOrder(request,link):
    orders = order.objects.get(id=link)
    form = orderForm(instance=orders)
    if request.method == 'POST':
        form = orderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, 'create_form.html',{'form':form})


@login_required(login_url='login')
def deleteOrder(request, link):
    orders = order.objects.get(id=link)
    if request.method == 'POST':
        orders.delete()
        return redirect('/')
    return render(request,'delete.html',{'item':orders})

@login_required(login_url='login')
def createCustomer(request):
    
    form = customerForm()

    return render(request,'create_form.html',{'form':form})


@login_required(login_url='login')
@allowed_user(allowed_roles='customer')
def userPage(request):
    orders = request.user.customer.order_set.all()
    count = orders.count()
    pending = orders.filter(status = 'pending').count()
    delivered = orders.filter(status = 'delivered').count()
    data = {
        'o':orders,
        'total_orders':count,
        'pending':pending,
        'delivered':delivered,
    }
    return render(request,'userPage.html',data)


@login_required(login_url='login')
@allowed_user(allowed_roles='customer')
def profSetting(request):
    customer = request.user.customer
    form = customerForm(instance=customer)

    if request.method == 'POST':
        form = customerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    return render(request, 'profile_set.html',{'data':form})