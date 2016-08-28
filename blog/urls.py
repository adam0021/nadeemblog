from django.conf.urls import url
from  . import views


urlpatterns=[
    url(r'^$',views.home,name='home'),

    url(r'^post/$',views.post_list,name='list'),

    url(r'^create/$',views.post_create,name='create'),
    url(r'^(?P<id>\d+)/$',views.post_detail,name='detail'),
    url(r'^edit/(?P<id>\d+)/$',views.post_update,name='update'),
    url(r'^delete/(?P<id>\d+)/$',views.post_delete,name='delete'),
    url(r'^(?P<id>\d+)/comment/$', views.add_comment, name='add_comment'),


]
