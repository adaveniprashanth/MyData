from django.db import models

# Create your models here.

class Task(models.Model):
    title= models.CharField(max_length=100)
    description=models.TextField(blank=True)
    completed=models.BooleanField(default=False,blank=True,null=True)

    def __str__(self): #this method will be used when we try to print the instance
        return self.title