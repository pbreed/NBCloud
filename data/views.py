from django.shortcuts import render
import math
from models import detector,shot
import datetime

def new_sample():
    #TODO build information input here.
    mydetector = detector.objects.get(device_id=)
    reading(detector=mydetector,vector=,start=,end=).save()
    solve()
    return "{'Success':True}"# match Fred's expectations here

def solve():
    #Where I need the mathmatic magic.

    #Currently adds a shot at kevin's house now.
    shot(gps_latitude=34.216601,gps_longitude=-118.251676,start=datetime.datetime.now(),end=(datetime.datetime.now()+datetime.timedelta(seconds=1))).save()
