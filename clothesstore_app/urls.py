from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.clothes_store, name='clothes'),
    path('replenish/<int:count>', views.replenish_products, name='replenish'),
]
