from django.shortcuts import render
from .models import Product, Message
from .serializers import ProductSerializer, MessageSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import generics, viewsets

# function based views
# list all the products (function based view)
@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def list_products(request):
    products = Product.objects.all()
    serializer_class = ProductSerializer(products, many=True)
    response_data = {
        'products': serializer_class.data
    }
    return Response(response_data)



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
class ClassProducts(APIView):
    # specific view level authentication
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    # show all products
    def get(self, request):
        products = Product.objects.all()
        serializer_class = ProductSerializer(products, many=True)
        return Response(serializer_class.data)
    
    # create a new product
    def post(self, request):
        serialized_data = ProductSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            product_saved = serialized_data.save()
            response_data = {
                "message": "Product {} is created successfully".format(product_saved.name),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


# Views for product details
class ClassProductDetails(APIView):
    # show details of a product
    def get(self, request, id):
        products = Product.objects.filter(id=id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    
    # update a product
    def put(self, request, id):
        product = Product.objects.get(id=id)
        serialized_data = ProductSerializer(product, data=request.data)
        if serialized_data.is_valid(raise_exception=True):
            product_saved = serialized_data.save()
            response_data = {
                "message": "Product {} is updated successfully".format(product_saved.name),
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # delete a specific product
    def delete(self, request, id):
        try:
            product = Product.objects.get(id=id)
            product_data = ProductSerializer(product).data
            product.delete()
            response_data = {
                'message': 'Product deleted successfully.',
                'deleted_product': product_data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        
        except Product.DoesNotExist:
            response_data = {
                'error': 'Product not found.'
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)
        
        
# Generics class views
# list all products
class GenericProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
# CRUD product
class GenericProductDetails(generics.RetrieveAPIView,
                            generics.UpdateAPIView,
                            generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
# special generic view to RUD a product
class GenericSpecialProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    


# Viewsets
class ProductViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ReadOnlyProductViewsets(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer