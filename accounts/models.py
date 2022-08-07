from contextlib import nullcontext
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class customer(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    dp = models.ImageField(default='blank_1.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
            return self.name



class tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
            return self.name


class product(models.Model):
    CATEGORY = (
        ('indoor','indoor'),
        ('outdoor','outdoor'),
    )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    category = models.CharField(max_length=200, null=True,choices=CATEGORY)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(tag)

    def __str__(self):
            return self.name

class order(models.Model):
    STATUS = (
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('delivered','delivered'),
    )

    customer = models.ForeignKey(customer,null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(product,null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null= True, choices=STATUS)

    def __str__(self):
            return self.product.name
    
