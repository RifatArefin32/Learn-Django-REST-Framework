from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response


# Create your views here.

# list all the products
def list_products(request):
    products = Product.objects.all()
    serialized_products = ProductSerializer(products)
    context = {
        'products': serialized_products.data
    }
    return Response(context)