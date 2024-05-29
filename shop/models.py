from django.db import models


class Product(models.Model):
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=300)

class Order(models.Model):
    items = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    total = models.CharField(max_length=200)

