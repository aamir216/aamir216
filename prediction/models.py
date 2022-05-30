from django.db import models
from django.core.exceptions import RequestAborted
from datetime import datetime
from django.contrib.auth.models import User

class Prediction(models.Model):    
    symbol = models.CharField(max_length = 20, blank=False)    
    current = models.DecimalField(max_digits = 14, decimal_places=  2)    
    last_closed = models.DecimalField(max_digits = 14, decimal_places=  2)
    volume = models.DecimalField(max_digits = 14, decimal_places=  0)
    average = models.DecimalField(max_digits = 14, decimal_places=  2)   

class Response(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True) 

class Visitor(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True) 
    ip = models.CharField(max_length = 15, blank=True)    
    location = models.CharField(max_length = 15, blank=True)