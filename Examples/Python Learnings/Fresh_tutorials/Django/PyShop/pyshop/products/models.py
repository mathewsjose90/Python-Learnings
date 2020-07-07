from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=3000)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    discount = models.FloatField()
