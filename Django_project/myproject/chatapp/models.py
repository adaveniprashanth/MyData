from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE),# when user deleted, then attached fileds in other tables also deleted
    name=models.CharField(max_length=100),
    pic=models.ImageField(upload_to="img",blank=True,null=True),#it will be ok if user  not provide image

    def __str__(self): # creates the name for the object instead of providing id
        return self.name
class Friend(models.Model):
    pass

