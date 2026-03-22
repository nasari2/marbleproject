from django.db import models
from user.models import User
from product.models import Product
# Create your models here.
class Order(models.Model):
    o_id = models.AutoField(primary_key=True)
    date_time = models.DateField()
    quantity = models.CharField(max_length=45)
    #u_id = models.IntegerField()
    u = models.ForeignKey(User,on_delete=models.CASCADE)
    #p_id = models.CharField(max_length=45)
    p = models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'order'
