from django.db import models

# Create your models here.
class Product(models.Model):
    sku = models.TextField(unique = True)
    name = models.CharField(max_length = 255)
    qty = models.IntegerField()
    price = models.FloatField()
