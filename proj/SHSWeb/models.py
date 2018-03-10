from django.db import models

# Create your models here.
class Students(models.Model):
    name= models.CharField(max_length=1000,blank=True,null=False)
    email= models.CharField(max_length=1000,blank=True,null=False)
    password=models.CharField(max_length=1000,blank=True,null=False)

    def __str__(self):
        return  self.name 