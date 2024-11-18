from django.urls import path, include
from .views import list_products, list_messages

urlpatterns = [
    path('product-list/', list_products, name='ListProduct'), # DRF authentication
    path('message-list/', list_messages, name='ListMessage'), 
]