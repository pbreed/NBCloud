from django.db import models

# Gunshot detection....

# Create your models here.
class detector(models.Model):
    device_id = models.CharField(max_length=30)
    gps_latitude = models.DecimalField(max_digits=14, decimal_places=9)
    gps_longitude = models.DecimalField(max_digits=14, decimal_places=9)
    humidity = models.DecimalField(max_digits=9, decimal_places=5)

class reading(models.Model):
    vector = models.DecimalField()
    start = models.DateTimeField()
    end = models.DateField()
    detector = models.ForeignKey('detector')

class shot(models.Model):
    gps_latitude = models.DecimalField(max_digits=14, decimal_places=9)
    gps_longitude = models.DecimalField(max_digits=14, decimal_places=9)
    start = models.DateTimeField()
    end = models.DateField()

