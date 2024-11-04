from django.db import models
from product.models import Product
# Create your models here.
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    # product_id = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cart'
