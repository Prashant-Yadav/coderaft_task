
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, default=None)
    sku = models.CharField(max_length=255, blank=True, null=True)
    inventory = models.IntegerField()
    image = models.ImageField(upload_to='images/coderaft/')

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, default=None)

    def __unicode__(self):
        return self.name


class Product(models.Model):
	# Connecting Product model with Category model
    product = models.ForeignKey(Product)
    category = models.ForeignKey(Category)
