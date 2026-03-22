from django.db import models

# Create your models here.
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    u_phone = models.CharField(max_length=45)
    u_email = models.CharField(max_length=500)
    u_place = models.CharField(max_length=20)
    u_post = models.CharField(max_length=10)
    u_district = models.CharField(max_length=15)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'


