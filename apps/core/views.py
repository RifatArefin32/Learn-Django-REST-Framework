from django.db.models import Max
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer

# list of all products 
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# list of all products with additional info
@api_view(['GET'])
def product_info_list(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data, status=status.HTTP_200_OK)

# product details
@api_view(['GET'])
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductInfoSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

# list of all orders
@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)