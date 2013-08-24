from django.conf.urls import patterns, url

from socialcrawl.networks import views

urlpatterns = patterns('',
    url(r'^v1/networks$', views.networks, name='networks'),
    url(r'^v1/profiles/(?P<network>\w+)$', views.profiles, name='profiles'),
    url(r'^v1/profiles/(?P<network>\w+)/(?P<username>\w+)$', views.profiles, name='profiles'),
)
