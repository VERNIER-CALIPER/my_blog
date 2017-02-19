from django.conf.urls import url
from . import views

app_name = 'shaozi_blog'
urlpatterns = [
    url(r'^(?P<type>\w+)/$', views.category , name='type'),
    url(r'^article/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})-(?p<pk>[0-9]+)/$'
         ,views.article,name='article'),
]
