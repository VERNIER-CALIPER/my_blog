from django.conf.urls import url
from . import views

app_name = 'shaozi_blog'
urlpatterns = [
    url(r'^$',views.index),
    url(r'^(?P<cate>\w+)/$', views.category , name='category'),
    url(r'^article/(?P<pk>[0-9]+)/$'
         ,views.article,name='article'),
]
