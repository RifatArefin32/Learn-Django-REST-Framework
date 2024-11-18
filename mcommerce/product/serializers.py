from rest_framework import serializers
from django.utils import timezone
from .models import Product

# model based serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name', 'price']
        # Note: `model` and `fields` are predefined keywords for model serializer
        

# simple serializer (does not depend on model)
# serializer for message
class MessageSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField(default=timezone.now) 