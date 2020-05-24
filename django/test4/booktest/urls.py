from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$',views.index),
    url(r'^(\d+)/(\d+)/$',views.show,name='show'),
    url(r'^base$',views.base,name='base'),
    url(r'^user$',views.user,name='user'),
    url(r'^user1$',views.user1,name='user1'),
    url(r'^htmlTest$',views.htmlTest,name='htmlTest'),
    url(r'^csrf1$',views.csrf1,name='scrf1'),
    url(r'^csrf2$',views.csrf2,name='scrf2'),
    url(r'^code1$',views.code1,name='code1'),
    url(r'^changeCode$',views.changeCode,name='changeCode'),
    url(r'^code2$',views.code2,name='code2'),
]
