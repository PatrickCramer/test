from django.shortcuts import render, get_object_or_404
from .models import Name, Adress
from datetime import datetime
import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    names = Name.objects.all()
    return render(request, 'namelist/index.html', {'names' : names, 'time':time()})

def adress(request, adress_id=1):
    adress = get_object_or_404(Adress, pk=adress_id)
    fulladress = 'Holland' + ' ' + adress.city + ' ' + adress.street

    return render(request, 'namelist/adress.html', {'adress': adress, 'time':time(), 'fulladress': fulladress})

def adress_edit(request, adress_id):
    adress = Adress.objects.get(pk=adress_id)
    return render(request, 'namelist/adress_edit.html', {'adress': adress, 'time':time()})

def adress_edit_submit(request, adress_id):
    adress = Adress.objects.get(pk=adress_id)
    # Hier moet street en city geupdate worden.. Hoe?
    adress.street = request.POST['street']
    adress.city = request.POST['city']
    adress.save()
    return HttpResponseRedirect(reverse('names:index'))


# Plaats de tijd in de footer
def time():
    now = datetime.datetime.now()
    t = now.strftime("%Y-%m-%d %H:%M")
    return t




