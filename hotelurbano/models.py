from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    original_id = models.IntegerField(default=0)
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='prod_images/')

class Offers(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='offers')
    original_id = models.IntegerField(default=0)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    daily = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    class Meta:
        ordering = ('price', 'product__title')

    def __str__(self):
        return self.title

class OffersOrigins(models.Model):
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE, related_name='offerorigin')
    origin_name = models.CharField(max_length=200)

    def __str__(self):
        return self.origin_name
