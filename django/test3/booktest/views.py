#-*-coding:utf8-*-
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

def test(request,a):
    return HttpResponse(a)

def index(request):
    return HttpResponse('HELLO WORLD')
def test(request):
    return HttpResponse('GOOD JOB')
def detail(request,num):
    return HttpResponse(num)
def arg(requset,p1,p2,p3):
    return HttpResponse(p1+'-'+p2+'-'+p3)
def kwarg(request,p1,p2):
    return HttpResponse(p1+':'+p2)
# Create your views here.
def getTest1(request):
    return render(request,'booktest/getTest1.html')
def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1,'b':b1,'c':c1}
    return render(request,'booktest/getTest2.html',context)
def getTest3(request):
    li = request.GET.getlist('a')
    context = {'list':li}

    return render(request,'booktest/getTest3.html',context)
def postTest1(request):
    return render(request,'booktest/postTest1.html')
def postTest2(request):
    uname=request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/postTest2.html',context)
from datetime import datetime

def cookie(request):
    response = HttpResponse()
    if request.COOKIES.has_key('h1'):
        response.write('<h1>'+request.COOKIES['h1']+'</h1>')
    # response.set_cookie('h1','hello',120)
    # response.set_cookie('h1','hello lby',None,datetime(2019,9,9))
    return response
    # if request.has_cookies:

def red1(request):
    # return HttpResponseRedirect('/booktest/red2')
    return redirect('/booktest/red2')
def red2(request):
    return HttpResponse('<h1>This is the new page</h1>')


def session_handler(request):

    uname = request.POST.get('uname')
    request.session['uname'] = uname
    request.session.set_expiry(0)
    return redirect('/booktest/session2')
def session1(request):
    return render(request,'booktest/session1.html')
def session2(request):
    uname = request.session.get('uname')
    context = {'uname':uname}
    return render(request,'booktest/session2.html',context)
def session3(request):
    del request.session['uname']
    return redirect('/booktest/session2')
