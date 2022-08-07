from . import views
from django.urls import path

urlpatterns = [
    
    path('products/',views.products, name='prod'),
    path('customer/<str:link>/',views.customers, name='customer'),
    path('orderForm/<str:link>',views.createOrder, name='Ocreate'),
    path('customerForm/',views.createCustomer, name='Ccreate'),
    path('update_order/<str:link>',views.updateOrder, name='update_order'),
    path('delete_order/<str:link>',views.deleteOrder, name='delete_order'),
    path('user/', views.userPage,name='user-page'),
    path('setting/',views.profSetting,name='setting')

]