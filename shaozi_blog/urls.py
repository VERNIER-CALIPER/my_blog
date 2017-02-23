from django.conf.urls import url
from . import views

app_name = 'shaozi_blog'
urlpatterns = [
    url(r'^$',views.index),
    url(r'^(?P<cate>\w+)/$', views.category , name='category'),
    url(r'^article/(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})-(?P<pk>[0-9]+)/$'
         ,views.article,name='article'),
]
