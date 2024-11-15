from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

# list all the products
@api_view(['GET'])
def list_products(request):
    products = Product.objects.all()
    serialized_products = ProductSerializer(products, many=True)
    context = {
        'products': serialized_products.data
    }
    return Response(context)