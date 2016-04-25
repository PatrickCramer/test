from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Name(models.Model):
    first_name =  models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.first_name

class Adress(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    img_house = models.ImageField(upload_to='files',blank=True)
    Name = models.ForeignKey(Name, on_delete=models.CASCADE)

    def __str__(self):
        return self.street










