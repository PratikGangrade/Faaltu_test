from django.contrib import admin
from .models import *

# Register your models here.
class cust(admin.ModelAdmin):
    
    list_display = ('name','phone','email','date_created')

admin.site.register(customer,cust)


class prod(admin.ModelAdmin):
    
    list_display = ('name','price','category','date_created')

admin.site.register(product,prod)

class Order(admin.ModelAdmin):
    
    list_display = ('customer','product','status','date_created',)

admin.site.register(order,Order)


admin.site.register(tag)
