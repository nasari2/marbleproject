from django.db import models
from user.models import User
# Create your models here.
class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=45)
    p_price = models.CharField(max_length=45)
    p_image = models.CharField(max_length=45)
    p_flavor = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'product'


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    # p_id = models.IntegerField()
    p=models.ForeignKey(Product,on_delete=models.CASCADE)
    # u_id = models.IntegerField()
    u=models.ForeignKey(User,on_delete=models.CASCADE)
    qty = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cart'

class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rating = models.CharField(max_length=45)
    # u_id = models.IntegerField()
    u=models.ForeignKey(User,on_delete=models.CASCADE)
    # p_id = models.IntegerField()
    p=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'rating'


