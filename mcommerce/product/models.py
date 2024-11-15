from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    expire_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    