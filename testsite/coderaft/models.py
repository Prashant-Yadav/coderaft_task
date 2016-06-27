from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30, default=None)
    sku
    inventory = models.IntegerField()
    image = models.


class Category(models.Model):
    name = models.CharField(max_length=30, default=None)
