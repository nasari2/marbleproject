from django.db import models
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=45)
    custom = models.CharField(max_length=45)
    products = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    user = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'event'

# Create your models here.
