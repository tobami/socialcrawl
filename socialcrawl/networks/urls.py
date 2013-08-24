from django.conf.urls import patterns, url

from socialcrawl.networks import views

urlpatterns = patterns('',
    url(r'^v1/networks$', views.networks, name='networks'),
    url(r'^v1/profiles/(?P<network>\w+)$', views.profile_list, name='profile_list'),
)
