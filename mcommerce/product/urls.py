from django.urls import path, include
from .views import list_products

urlpatterns = [
    path('product-list/', list_products, name='ListProduct'), # DRF authentication
]