from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rooms(models.Model):
    ROOM_TYPES=(('ac','AC'),('nonac','NonAc'))
    BED_TYPES=(('single','SINGLE'),('double','DOUBLE'))
    STATUS=(('booked','BOOKED'),('available','AVAILABLE'))
    roomno=models.IntegerField(primary_key=True)
    roomtype=models.CharField(max_length=6,choices=ROOM_TYPES,default='ac')
    bedtype=models.CharField(max_length=7,choices=BED_TYPES,default='single')
    status=models.CharField(max_length=10,choices=STATUS,default='available')
    class Meta:
        ordering=('roomno',)
        verbose_name_plural="rooms"
    def __str__(self):
        return self.roomtype
class hotelusers(User):
    class Meta:
        proxy=True
        verbose_name_plural="hotelusers"

class urequests(models.Model):
    ROOM_TYPES=(('ac','AC'),('nonac','NonAc'))
    BED_TYPES=(('single','SINGLE'),('double','DOUBLE'))
    name=models.CharField(max_length=64)
    mobile=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    roomtype=models.CharField(max_length=6,choices=ROOM_TYPES,default='ac')
    bedtype=models.CharField(max_length=7,choices=BED_TYPES,default='single')

    class Meta:
        ordering=('name',)
        verbose_name_plural="userrequests"

    def __str__(self):
        return self.name
