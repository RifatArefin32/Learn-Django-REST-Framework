from django.urls import path, include
from .views import list_products, list_messages
from .views import ClassProducts, ClassProductDetails
from .views import GenericProducts, GenericProductDetails

urlpatterns = [
    path('product-list/', list_products, name='ListProduct'), # DRF authentication
    path('message-list/', list_messages, name='ListMessage'), 
    
    # class based view
    path('class-product-list/', ClassProducts.as_view(), name='class_products'),
    path('class-product-detail/<int:id>/', ClassProductDetails.as_view(), name='class_product_details'),
    
    # generic view
    path('generic-product-list/', GenericProducts.as_view(), name='generic_products'),
    path('generic-product-detail/<int:id>/', GenericProductDetails.as_view(), name='generic_product_details'),
]