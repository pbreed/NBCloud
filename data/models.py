from django.db import models

class device(models.Model):
    id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    gps_latitude = models.DecimalField(max_digits=14, decimal_places=9)
    gps_longitude = models.DecimalField(max_digits=14, decimal_places=9)

    def tojson(self):
        json = {'name':self.name,
                'location':{
                    'location_name':self.location,
                    'gps_latitude':str(self.gps_latitude),
                    'gps_longitude':str(self.gps_longitude)}
                }
        return json

class channel(models.Model):
    name = models.CharField(max_length=30)
    device = models.ForeignKey('device')
    channel = models.IntegerField()

    # DO I make this call the device from here to JSONify device? how many nestings do I want here?
    def tojson(self):
        json = {'name':self.name}
        return json

class sample(models.Model):
    value = models.DecimalField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    channel = models.ForeignKey('channel')

    def tojson(self):
        json = {
                'device':self.channel.device.tojson(),
                'channel':self.channel.tojson(),
                'start':str(self.start),
                'end':str(self.end),
                'value': str(self.value)
                }
        return json
