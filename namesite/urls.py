"""namesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('namelist.urls', namespace="names")),
    url(r'^', include('tasks.urls', namespace="tasks")),
    url(r'^', include('blog.urls', namespace="blog")),
    url(r'^', include('weather.urls', namespace="weather")),
    url(r'^', include('hackernews.urls', namespace="hackernews")),
    url(r'^', include('scraper.urls', namespace="scraper")),
    url(r'^', include('bootstrap.urls', namespace="bootstrap")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
