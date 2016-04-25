from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tasks/$', views.index, name='index'),
    # 127.0.0.1/tasks
    url(r'^tasks/(?P<name_id>[0-9]+)/edit/$', views.taskedit, name='taskedit'),
    # 127.0.0.1/tasks/1/edit
    url(r'^tasks/(?P<name_id>[0-9]+)/$', views.task, name='task'),
    # 127.0.0.1/tasks/1
    url(r'^tasks/(?P<name_id>[0-9]+)/task_new$', views.task_new, name='task_new'),
    # 127.0.0.1/tasks/1/task_new







]