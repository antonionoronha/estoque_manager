from .views import product_list, product_form, purchase_form, purchase_list
from django.urls import path, include

app_name = 'core'

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('', product_list, name='home'),
    path('product/list', product_list, name='product_list'),
    path('purchase/list', purchase_list, name='purchase_list'),
    path('product/create', product_form, name='product_form'),
    path('purchase/create', purchase_form, name='purchase_form')
]
