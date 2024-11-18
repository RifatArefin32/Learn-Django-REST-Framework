from django.urls import path, include
from .views import list_products, list_messages
from .views import ClassProducts

urlpatterns = [
    path('product-list/', list_products, name='ListProduct'), # DRF authentication
    path('message-list/', list_messages, name='ListMessage'), 
    path('class-product-list/', ClassProducts.as_view(), name='class_products'),
]