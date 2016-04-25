from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 127.0.0.1/

    url(r'^adress/$', views.adress, name='adress'),
    # 127.0.0.1/adress

    url(r'^adress/(?P<adress_id>[0-9]+)/$', views.adress, name='adress2'),
    # 127.0.0.1/adress/1

    url(r'^adress/edit/(?P<adress_id>[0-9]+)/$', views.adress_edit, name='adress_edit'),
    # 127.0.0.1/adress/edit/1

    url(r'^adress/adress_edit/(?P<adress_id>[0-9]+)/$', views.adress_edit_submit, name='adress_edit_submit'),
    # 127.0.0.1/adress/adress_edit/1

]


