from django.db import models
from cart.models import Cart
from product.models import Product
from customer.models import Customer

# Create your models here.

class Checkout(models.Model):
    checkout_id = models.AutoField(primary_key=True)
    # cart_id = models.IntegerField()
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    # product_id = models.IntegerField()
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    # customer_id = models.IntegerField()
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'checkout'

