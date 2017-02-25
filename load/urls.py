from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^complaint/$',views.complain),
    url(r'^login/$',views.login`1   ),
]
