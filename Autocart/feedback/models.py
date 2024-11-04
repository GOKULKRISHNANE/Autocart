from django.db import models
from customer.models import Customer

# Create your models here.


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=45)
    # customer_id = models.IntegerField()
    Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'feedback'

