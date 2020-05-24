# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from models import *
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from hashlib import sha1
# Create your views here.
def register(req):
    return render(req,'df_user/register.html',{})
def register_handle(req):
    post = req.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    if upwd != upwd2:
        return redirect('df_user/register.html')
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    return redirect('df_user/login.html')
def register_exist(req):
    uname = req.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})
def login(req):
    uname = req.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(req,'df_user/login.html',context)
def login2(req):
    uname = req.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(req,'df_user/login2.html',context)
def login2_handle(req):
    post = req.POST
    uname = post['uname']
    upwd = post['upwd']
    print(uname,upwd)
    users = UserInfo.objects.filter(uname=uname)
    if len(users)==1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].upwd:
            return HttpResponseRedirect('/user/info/')
        else:
            return JsonResponse({'error_pwd':1})
    else:
        return JsonResponse({'error_name':1})
def login2_exist(req):
    post = req.POST
    print(post[uname],post[upwd]);

def login_handle(req):
    post = req.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    memory = post.get('memory')
    users = UserInfo.objects.filter(uname=uname)
    print(uname)
    if len(users)==1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].upwd:
            red = HttpResponseRedirect('/user/info/')
            if memory != 0 :
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            req.session['user_id']=users[0].id
            req.session['user_name']=uname
            return red
        else:
            context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(req,'df_user/login.html',context)
    else:
        context = {'title':'用户登录','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
        return render(req,'df_user/login.html',context)


def info(req):
    '''
    user_eamil = UserInfo.objects.get(id=req.session['user_id']).uemail
    context={'title':'用户中心',
            'user_email':user_email,
            'user_name':req.session(['user_name'])
            }
    '''
    return render(req,'df_user/user_center_info.html',{'title':'用户中心'})
def order(req):
    return render(req,'df_user/user_center_order.html',{'title':'用户中心'})
def site(req):
    return render(req,'df_user/user_center_site.html',{'title':'用户中心'})
def login(req):
    return render(req,'df_user/login.html',{'title':'天天生鲜-登陆'})

