from django.db import models


class Product(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=300)



