# Create your models here.
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    blog_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.blog_text

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
    blog = models.ForeignKey(Blog)

    def __str__(self):
        return self.comment




