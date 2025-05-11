import random
from django.core.management.base import BaseCommand
from faker import Faker
from apps.accounts.models import CustomUser
from apps.core.models import Product, Order, OrderItem

fake = Faker()

class Command(BaseCommand):
    help = 'Populate dummy data'

    def handle(self, *args, **kwargs):
        # Create dummy users
        # 5 users have already been created [./accounts/management/commands/dummy_users.py]

        # Create 10 dummy products
        products = []
        for _ in range(10):
            product = Product.objects.create(
                name=fake.word().capitalize(),
                description=fake.text(),
                price=round(random.uniform(10.0, 100.0), 2),
                stock=random.randint(1, 50)
            )
            products.append(product)
        self.stdout.write(self.style.SUCCESS("Created 10 products."))

        # Create dummy orders with order items
        user = CustomUser.objects.get(id=1)
        
        for _ in range(random.randint(1, 3)):
            order = Order.objects.create(user=user)
            selected_products = random.sample(products, k=random.randint(1, 4))
            for product in selected_products:
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=random.randint(1, 5)
                )
        self.stdout.write(self.style.SUCCESS("Created orders with order items."))