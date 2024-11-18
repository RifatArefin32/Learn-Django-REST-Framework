from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# list all the products (function based view)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list_products(request):
    products = Product.objects.all()
    serialized_products = ProductSerializer(products, many=True)
    context = {
        'products': serialized_products.data
    }
    return Response(context)