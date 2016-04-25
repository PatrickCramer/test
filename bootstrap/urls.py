from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bootstrap/$', views.index, name='index'),
    url(r'^bootstrap/$', views.index, name='boot2'),
]