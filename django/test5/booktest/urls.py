from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^myexp$',views.MyExp),
    url(r'^uploadpic$',views.uploadPic),
    url(r'^uploadHandle$',views.uploadHandle),
    url(r'^herolist(\d*)/$',views.herolist),
    url(r'^area$',views.getArea),
    url(r'^area1/$',views.getArea1),
    url(r'^(\d+)/$',views.getArea2),
    url(r'^html/$',views.html),
    url(r'^htmlHandler/$',views.htmlHandler,name='htmlHandler'),
    url(r'^html2/$',views.html2),
    url(r'^cache1/$',views.cache1),
    url(r'^mysearch/$',views.mysearch),
    url(r'^last/$',views.last),
]
