from django.db import models
from customer.models import Customer


# Create your models here.

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    # customer_id = models.IntegerField()
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    bill_id = models.IntegerField()
    type = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    cart_number = models.CharField(max_length=45)
    cvv = models.IntegerField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'payment'
