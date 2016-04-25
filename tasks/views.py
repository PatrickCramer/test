from django.shortcuts import render
from models import Task
from namelist.models import Name
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    print 'hij komt bij INDEX'
    name = Name.objects.all()
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'name' : name, 'tasks': tasks})

def task(request, name_id):
    print 'hij komt bij task'
    tasks = Task.objects.filter(Name_id = name_id)
    return render(request, 'tasks/list.html', {'tasks' : tasks})

def task_new(request, name_id):
    print 'hij komt bij task_new'
    tasks = Task.objects.filter(Name_id=name_id)
    Task.objects.create(todo='', Name_id=name_id)
    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskedit(request, name_id):
    r = request.POST
    d = dict(r)
    for k,v in d.items():
        try:
            int(k)
            t = Task.objects.get(pk=k)
            t.todo = v[0]
            t.save()
        except:
            pass

    return HttpResponseRedirect(reverse('names:index'))

