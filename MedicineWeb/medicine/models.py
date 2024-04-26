from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    quantity = models.IntegerField(null=True)
    description = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title