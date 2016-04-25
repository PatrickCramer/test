from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    print 'hij komt bij INDEX'
    somedata = 'bla'
    return render(request, 'bootstrap/index.html', {'somedata' : somedata})
