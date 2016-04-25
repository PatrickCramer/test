from __future__ import unicode_literals

from django.db import models

class Volkskrant(models.Model):

    linklist = models.CharField(max_length=20000)

    def __str__(self):
        return self.linklist

