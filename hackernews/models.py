from __future__ import unicode_literals

from django.db import models


class Hn(models.Model):

    All_items_dict = models.CharField(max_length=20000)

    def __str__(self):
        return self.All_items_dict


