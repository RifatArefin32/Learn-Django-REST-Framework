from rest_framework import serializers
from .models import Product

# model based serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name', 'price']
        # Note: `model` and `fields` are predefined keywords for model serializer