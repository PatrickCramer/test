from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.index, name='index'),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', views.comment, name='comment'),
    url(r'^blog/(?P<blog_id>[0-9]+)/comment_submit/$', views.comment_submit, name='comment_submit'),
    url(r'^blog/blog_entry/$', views.blog_entry, name='blog_entry'),
]

# 127.0.0.1/blog

    # url(r'^tasks/(?P<name_id>[0-9]+)/edit/$', views.taskedit, name='taskedit'),
    # 127.0.0.1/tasks/1/edit
    # url(r'^tasks/(?P<name_id>[0-9]+)/$', views.task, name='task'),
    # 127.0.0.1/tasks/1

