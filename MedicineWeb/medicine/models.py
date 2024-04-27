from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
    ('Dhaka', 'Dhaka'),
    ('Rangpur', 'Rangpur'),
    ('Chattogram', 'Chattogram'),
    ('Rajshai', 'Rajshai'),
    ('Khulna', 'Khulna'),
    ('Barishal', 'Barishal'),
    ('Mymensingh', 'Mymensingh')
)

CATEGORY_CHOICES = (
    ('CL', 'Cold'),
    ('EY', 'Eye'),
    ('DT', 'Dehydration'),
    ('HT', 'Heat Stroke'),
    ('SA', 'Seasonal allergies'),
    ('TP', 'Typhoid'),
    ('OT', 'Other')
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    quantity = models.IntegerField(null=True)
    description = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=200)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


@property
def total_cost(self):
    return self.quantity * self.product.discounted_price


STATUS_CHOICES = (
    ('accpected', 'accpected'),
    ('packed', 'packed'),
    ('On the way', 'on the way'),
    ('Deliverd', 'Deliverd'),
    ('pending', 'pending'),
)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    bikaspay_order_id = models.CharField(max_length=100, blank=True, null=True)
    bikaspay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    bikas_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)


class OrderPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")

    @property
    def total_cost(self):
        return self.quantity * self.product_discounted_price
