from django.db import models
from datetime import datetime
# Create your models here.

# defining the model so that we can access in views.py file
class feature:
    id:int
    name:str
    description:str

# database sample
# to work this code we have to migrate by following commands
# we have to  inform django that the app is installed . we can do this in settings.py file INSTALLED_APPS
# python manage.py makemigrations
# python manage.py migrate
# admin user is admin and password is prashanth
# next we have register this model in admin.py
class design(models.Model):
    name = models.CharField(max_length=50)
    description=models.CharField(max_length=100)


class Post(models.Model):
    title=models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=datetime.now(),blank=True)

class Room(models.Model):
    name=models.CharField(max_length=150)

class Message(models.Model):
    value=models.CharField(max_length=1000000,)
    sent_at=models.DateTimeField(default=datetime.now(),blank=True)
    user=models.CharField(max_length=1000)#to store the user name who sent the message
    room_name=models.CharField(max_length=150)#to which room the user has connected

