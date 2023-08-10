from django.db import models
from datetime import datetime,time
from django.utils import timezone

# Create your models here.

class ScreenShot(models.Model):
    host=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    created_at=models.DateTimeField(auto_now_add=True)
    screen_name=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.image.name
    
    def save(self, *args, **kwargs):
        super(ScreenShot, self).save(*args, **kwargs)

# default=timezone.now().replace(hour=9, minute=00, second=0),



class User(models.Model):
    username=models.CharField(max_length=100,unique=True,default=None,null=True,blank=True)
    host=models.CharField(max_length=70)
    start_time=models.DateTimeField(null=True,blank=True)
    end_time=models.DateTimeField(null=True,blank=True)
    ss_count=models.IntegerField(default=3,null=True,blank=True)
    time_gap=models.IntegerField(default=1,null=True,blank=True)

    def __str__(self):
        return self.host


class EventOff(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pre_off_time=models.DateTimeField()
    post_off_time=models.DateTimeField()
    
    def __str__(self):
        return f"{self.user} - {self.pre_off_time}"
    
    
    