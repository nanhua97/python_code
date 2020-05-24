from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^\(\d+\)$',views.test),
    #url(r'^(\d+)$',views.detail),
    url(r'^abc/(?P<num>\d+)/$',views.detail),
    url(r'^(\d+)/(\d+)/(\d+)$',views.arg),
    url(r'^(?P<p2>\d+)/(?P<p1>\d+)$',views.kwarg),
    url(r'^getTest1/$',views.getTest1),
    url(r'^getTest2/$',views.getTest2),
    url(r'^getTest3/$',views.getTest3),
    url(r'^postTest1$',views.postTest1),
    url(r'^postTest2$',views.postTest2),
    url(r'cookies$',views.cookie),
    url(r'^red1$',views.red1),
    url(r'^red2$',views.red2),
    url(r'^session1$',views.session1),
    url(r'^session2$',views.session2),
    url(r'^session3$',views.session3),
    url(r'^session_handler$',views.session_handler),

]

