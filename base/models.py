from django import views
from django.db import models

# Create your models here.
class userData(models.Model):
    device_os = models.CharField(max_length=200,null=True,blank=True)
    device_browser = models.CharField(max_length=200,null=True,blank=True)
    device_type = models.CharField(max_length=200,null=True,blank=True)
    device_model = models.CharField(max_length=200,null=True,blank=True)

    site_url = models.CharField(max_length=200,null=True,blank=True)
    referrer_url = models.CharField(max_length=200,null=True,blank=True) # should be larger string - dynamic needed

    user_agent = models.CharField(max_length=1000,null=True,blank=True) # should be larger string - dynamic needed
    timestamp = models.CharField(max_length=200,null=True,blank=True)
    timezone = models.CharField(max_length=200,null=True,blank=True)

    location_longitude = models.CharField(max_length=200,null=True,blank=True)
    location_latitude = models.CharField(max_length=200,null=True,blank=True)
    location_country = models.CharField(max_length=200,null=True,blank=True)
    location_region = models.CharField(max_length=200,null=True,blank=True)
    location_city = models.CharField(max_length=200,null=True,blank=True)
    location_zip = models.CharField(max_length=200,null=True,blank=True)

    user_ip = models.CharField(max_length=200,null=True,blank=True)

    views = models.IntegerField(null=True, blank=True,default=1)

    user_id = models.CharField(max_length=300,null=True,blank=True)
    device_id = models.CharField(max_length=300,null=True,blank=True)

    _id = models.AutoField(primary_key=True,editable=False) 

    
    
    
