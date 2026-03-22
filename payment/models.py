from django.db import models
from user.models import User
from order.models import Order
# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    #u_id = models.IntegerField()
    u = models.ForeignKey(User,on_delete=models.CASCADE)
    #o_id = models.IntegerField()
    o = models.ForeignKey(Order,on_delete=models.CASCADE)
    amount = models.CharField(max_length=45)
    date_time = models.DateField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'payment'
