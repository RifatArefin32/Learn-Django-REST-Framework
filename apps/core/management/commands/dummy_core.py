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
        users = []
        for _ in range(5):
            user = CustomUser.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
            users.append(user)
        self.stdout.write(self.style.SUCCESS("✅ Created 5 users."))

        # Create dummy products
        products = []
        for _ in range(10):
            product = Product.objects.create(
                name=fake.word().capitalize(),
                description=fake.text(),
                price=round(random.uniform(10.0, 100.0), 2),
                stock=random.randint(1, 50)
            )
            products.append(product)
        self.stdout.write(self.style.SUCCESS("✅ Created 10 products."))

        # Create dummy orders with order items
        for user in users:
            for _ in range(random.randint(1, 3)):
                order = Order.objects.create(user=user)
                selected_products = random.sample(products, k=random.randint(1, 4))
                for product in selected_products:
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=random.randint(1, 5)
                    )
        self.stdout.write(self.style.SUCCESS("✅ Created orders with order items."))