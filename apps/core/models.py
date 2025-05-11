import uuid 
from django.db import models
from apps.accounts.models import CustomUser

# Product model
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    # property is also considered as another field of the model
    @property
    def in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return self.name
    

# Order class
class Order(models.Model):
    class statusChoices(models.TextChoices):
        PENDING = 'Pending'
        CONFIRMED = 'Confirmed'
        CANCELLED = 'Cancelled'
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Product = models.ManyToManyField(Product, through="OrderItem", related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=statusChoices.choices, default=statusChoices.PENDING)

    def __str__(self):
        return f"Oder {self.order_id} By {self.user.username}"


# OrderItem class
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} X {self.product.name} in order {self.order.order_id}" 