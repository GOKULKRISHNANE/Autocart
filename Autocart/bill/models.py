from django.db import models
from customer.models import Customer

class Bill(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    bill_amount = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=45)
    # cust_id = models.CharField(max_length=45)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'bill'
