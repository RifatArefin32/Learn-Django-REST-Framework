from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    expire_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name


class Message:
    messages = []  # Static list to store all messages

    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created_at = created or datetime.now()
    
    def save(self):
        # Simulate saving the object (add it to the messages list)
        Message.messages.append(self)

    @classmethod
    def all(cls):
        # Return all stored messages
        return cls.messages