import random
from django.core.management.base import BaseCommand
from faker import Faker
from apps.accounts.models import CustomUser

fake = Faker()

class Command(BaseCommand):
    help = "Populate dummy users"

    def handle(self, *args, **options):
        # Create 5 dummy users
        users = []
        for _ in range(5):
            username = fake.user_name()
            email = fake.email()
            phone_number = fake.phone_number()
            gender = random.choice(['male', 'female'])
            
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password='password',  # Set a default password
                phone_number=phone_number,
                gender=gender
            )

            users.append(user)
        self.stdout.write(self.style.SUCCESS("5 users created"))
    
    