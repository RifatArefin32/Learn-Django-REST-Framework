from django.shortcuts import render
from .models import Product, Message
from .serializers import ProductSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# function based views
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



# list all message and create a message
@permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def list_messages(request):
    if request.method == 'GET':
        # List all messages
        messages = Message.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # Create a new message
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            message = Message(
                email=serializer.validated_data['email'],
                content=serializer.validated_data['content']
            )
            message.save()  # Save the message
            return Response(serializer.data, status=201)
        
        error_response = {
            'status': False,
            'errors': serializer.errors
        }
        return Response(error_response, status=400)
    
    
    
# class based views 
# Views for listing all products
class ClassProducts(APIView):
    # get all products
    def get(self, request):
        products = Product.objects.all()
        serializer_class = ProductSerializer(products, many=True)
        return Response(serializer_class.data)
    

class ClassProductDetails(APIView):
    def get(self, request, id):
        products = Product.objects.filter(id=id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)