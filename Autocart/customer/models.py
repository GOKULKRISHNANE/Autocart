from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=45)
    field_customer_phonenumber = models.CharField(db_column=' customer_phonenumber', max_length=45)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    customer_dateofbirth = models.DateField(blank=True, null=True)
    customer_gender = models.CharField(max_length=45)
    customer_username = models.CharField(max_length=45)
    customer_password = models.CharField(max_length=45)
    customer_address = models.CharField(max_length=45)
    customer_city = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'customer'


    class Meta:
        managed = False
        db_table = 'customer'
