# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Hn
import pickle

# Create your views here.

def index(request):

    # get dict from db
    hn_db = Hn.objects.get(id=1)
    hn_db = hn_db.All_items_dict

    # get dict from file
    file = open('/Users/Pat/PycharmProjects/MyProj/namesite/file_hn.txt', 'r')
    hn_file = pickle.load(file)
    file.close()

    return render(request, 'hackernews/index.html', {'hn_db':hn_db, 'hn_file':hn_file})


