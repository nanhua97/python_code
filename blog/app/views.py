# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def base(req):
    return render(req,'base.html',{})
def toRegister(req):
    return render(req,'register.html',{})
def toLogin(req):
    return render(req,'toLogin.html',{})
def login(req):
    return render(req,'login.html',{})
