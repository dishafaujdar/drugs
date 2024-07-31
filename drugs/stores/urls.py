from django.contrib import admin
from django.urls import path
from . import views

# localhost:8000/stores
# localhost:8000/stores/order => path('order/',views.orders, name='order'),  

urlpatterns = [
    path('',views.all_store, name='store_home'), 
]
