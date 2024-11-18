from django.urls import path, include
from .views import list_products, list_messages
from .views import ClassProducts, ClassProductDetails
from .views import GenericProducts, GenericProductDetails, GenericSpecialProductDetails
from .views import ProductViewsets, ReadOnlyProductViewsets
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('product-viewset', ProductViewsets, basename='product')
router.register('readonly-product-viewset', ReadOnlyProductViewsets, basename='readonly-product')


urlpatterns = [
    path('product-list/', list_products, name='ListProduct'), # DRF authentication
    path('message-list/', list_messages, name='ListMessage'), 
    
    # class based view
    path('class-product-list/', ClassProducts.as_view(), name='class_products'),
    path('class-product-detail/<int:id>/', ClassProductDetails.as_view(), name='class_product_details'),
    
    # generic view
    path('generic-product-list/', GenericProducts.as_view(), name='generic_products'),
    path('generic-product-detail/<int:pk>/', GenericProductDetails.as_view(), name='generic_product_details'), # note: generic url expects 'pk' as query parament
    path('generic-special-product-detail/<int:pk>/', GenericSpecialProductDetails.as_view(), name='generic_special_product_details'), # note: generic url expects 'pk' as query parament 
] + router.urls