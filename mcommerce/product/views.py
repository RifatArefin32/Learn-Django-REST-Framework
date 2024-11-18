from django.shortcuts import render
from .models import Product, Message
from .serializers import ProductSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# list all the products (function based view)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def list_products(request):
    products = Product.objects.all()
    serializer_class = ProductSerializer(products, many=True)
    context = {
        'products': serializer_class.data
    }
    return Response(context)

@api_view(['GET', 'POST'])
def list_messages(request):
    message_obj = Message('rifat@mcommerce.com', 'Test message')
    serializer_class = MessageSerializer(message_obj, many=False)
    
    return Response(serializer_class.data)