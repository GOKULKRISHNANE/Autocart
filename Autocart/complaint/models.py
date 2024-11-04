from django.db import models
from customer.models import Customer

# Create your models here.


class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=45)
    replay = models.CharField(max_length=45)
    # customer_id = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'complaint'
