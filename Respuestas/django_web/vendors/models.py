from django.db import models

# Create your models here.
class Vendor(models.Model):
    vendorid = models.TextField()
    tpep_pickup_datetime = models.TextField()
    trip_distance = models.TextField()
    payment_type = models.TextField(default='this is cool')