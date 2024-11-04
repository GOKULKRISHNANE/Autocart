from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    #category_id = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=45)
    product_photo = models.CharField(max_length=500)
    product_price = models.CharField(max_length=45)
    product_quantity =models.CharField(max_length=45)
    manufacturer_date = models.CharField(max_length=45)
    product_experity = models.CharField(max_length=45)

    additional_description = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'product'

