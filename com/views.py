from email.headerregistry import Group
from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm as ucf
from accounts.forms import CreateUserForm as cuf
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.decorators import *


@unauthenticated_user
def register(request):
    form = cuf()
    if request.method == 'POST':
        form = cuf(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Registered Successfully')
            return redirect('login')
    return render(request,'signup.html',{'form':form})


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        pwd = request.POST.get('upass')
        
        users = authenticate(request, username=name, password=pwd)

        if users is not None:
            auth_login(request, users)
            return redirect('/')
        messages.info(request, "username or password is invalid")
        return redirect('login')

    return render(request,'login.html')

def logOut(request):
    auth_logout(request)
    return redirect('login')



@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def home(request):
    
    orders = order.objects.all()
    total_orders = orders.count()
    last5 = total_orders - 5
    recent_orders = order.objects.all()[last5:total_orders]
    customers = customer.objects.all()
    
    total_customer = customers.count()
    delivered = orders.filter(status = 'delivered').count()
    pending = orders.filter(status = 'pending').count()

    data = {
        'order':orders,
        'customer':customers,
        'total_orders':total_orders,
        'l5':recent_orders,
        'total_customer':total_customer,
        'delivered':delivered,
        'pending':pending,
    }

    return render(request,'index.html',data)





        
