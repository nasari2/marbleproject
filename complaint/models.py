from django.db import models
from user.models import User
from order.models import Order
# Create your models here.

class Complaint(models.Model):
    c_id = models.AutoField(primary_key=True)
    #u_id = models.IntegerField()
    u = models.ForeignKey(User,on_delete=models.CASCADE)
    #o_id = models.CharField(max_length=45)
    o = models.ForeignKey(Order,on_delete=models.CASCADE)
    complaint = models.CharField(max_length=45)
    reply = models.CharField(max_length=100)
    date_time = models.DateField()

    class Meta:
        managed = False
        db_table = 'complaint'
