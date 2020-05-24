from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'register/$',views.register),
    url(r'register_handle/$',views.register_handle),
    url(r'register_exist/$',views.register_exist),
    url(r'login/$',views.login),
    url(r'login_handle/$',views.login_handle),
    url(r'login2/$',views.login2),
    url(r'login2_handle/$',views.login2_handle),
    url(r'login2_exist/$',views.login2_exist),
    url(r'info/$',views.info),
    url(r'order/$',views.order),
    url(r'site/$',views.site),

]

