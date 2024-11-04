from django.db import models


# Create your models here.

class StaffRegister(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=45)
    staff_address = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    staff_phonenumber = models.CharField(max_length=45)
    staff_dateofbirth = models.CharField(max_length=45)
    staff_gender = models.CharField(max_length=45)

    staff_email = models.CharField(max_length=45)
    user_name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'staff_register'
