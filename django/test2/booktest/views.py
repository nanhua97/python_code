#-*-coding:utf8-*-
from django.shortcuts import render
from .models import *
from django.db.models import Max,F,Q

def index(request):
    # list = BookInfo.books2.filter(heroinfo__hcontent__contains='六')
    #list = BookInfo.books2.aggregate(Max('pk'))
    #list = BookInfo.books2.filter(bread__gt = F('bcommet'))
    list = BookInfo.books2.filter(Q(pk__gt=3)|Q(heroinfo__hname__contains = '段'))
    contains={'list':list}
    return render(request,'booktest/index.html',contains)

# Create your views here.

