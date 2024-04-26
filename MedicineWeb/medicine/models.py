from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Rangpur','Rangpur'),
    ('Chattogram','Chattogram'),
    ('Rajshai','Rajshai'),
    ('Khulna','Khulna'),
    ('Barishal','Barishal'),
    ('Mymensingh','Mymensingh')
)


CATEGORY_CHOICES = (
    ('CL','Cold'),
    ('EY','Eye'),
    ('DT','Dehydration'),
    ('HT','Heat Stroke'),
    ('SA','Seasonal allergies'),
    ('TP','Typhoid'),
    ('OT','Other')
)


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

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=200)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

@property
def total_cost(self):
    return self.quantity*self.product.discounted_price