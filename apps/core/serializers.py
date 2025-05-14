from decimal import Decimal
from rest_framework import serializers
from apps.accounts.models import CustomUser
from .models import Product, Order, OrderItem

# product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'stock'
        )

    # custom field level validation
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than zero"
            )
        return value

# product info serializer 
class ProductInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()


# order item serializer
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2)

    class Meta:
        model = OrderItem
        fields = ['product', 'product_name', 'product_price', 'quantity', 'order', 'item_subtotal']


# user info serializer
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number', 'gender']


# order serializer (nested serializer)
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = UserInfoSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()
    total_price2 = serializers.SerializerMethodField(method_name='calc_total_price')

    class Meta:
        model = Order
        fields = ['order_id', 'user', 'created_at', 'status', 'items', 'total_price', 'total_price2']

    def get_total_price(self, obj):
        items = obj.items.all()
        total = Decimal('0.0')
        for item in items:
            total += item.item_subtotal
        return total
    
    def calc_total_price(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
