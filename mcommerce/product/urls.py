from django.urls import path, include
from .views import list_products, list_messages
from .views import ClassProducts, ClassProductDetails
from .views import GenericsProducts

urlpatterns = [
    path('product-list/', list_products, name='ListProduct'), # DRF authentication
    path('message-list/', list_messages, name='ListMessage'), 
    path('class-product-list/', ClassProducts.as_view(), name='class_products'),
    path('class-product-detail/<int:id>/', ClassProductDetails.as_view(), name='class_product_details'),
    path('generics-product-list/', GenericsProducts.as_view(), name='generics_products'),
]