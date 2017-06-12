from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='subscribe'),
    #url(r'^subscribe/$', views.subscribe, name='subscribe'),
]