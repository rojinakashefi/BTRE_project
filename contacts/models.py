from django.db import models
from datetime import datetime

class Contact(models.Model):
    name =  models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now,blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name
