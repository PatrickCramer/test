from __future__ import unicode_literals
from django.db import models
from namelist.models import Name

# Create your models here.


class Task(models.Model):

    todo = models.CharField(max_length=200)
    done = models.CharField(max_length=100)
    Name = models.ForeignKey(Name)

    def __str__(self):
        return self.todo
