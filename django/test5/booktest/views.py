import os
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from .models import *
from django.core.paginator import *
def index(request):
    return render(request,'booktest/index.html')
# Create your views here.
def MyExp(request):
    a=int('abc')
    return HttpResponse('hello')
def uploadPic(request):
    return render(request,'booktest/uploadPic.html')
def uploadHandle(request):
    pic1 = request.FILES['pic1']
    picName=os.path.join(settings.MEDIA_ROOT,pic1.name)
    with open(picName,'wb+') as pic:
        for c in pic1.chunks():
            pic.write(c)
    return HttpResponse('<img src="/static/media/%s">'%pic1.name)

#分页
def herolist(request,pindex):
    if pindex == '':
        pindex = '1'
    list = HeroInfo.objects.all()
    paginator = Paginator(list,5)
    page = paginator.page(int(pindex))
    context={'page':page}
    return render(request,'booktest/herolist.html',context)

def getArea(request):
    return render(request,'booktest/area1.html')
def getArea1(request):
    list = Areas.objects.filter(parea__isnull=True)
    list2=[]
    for a in list:
        list2.append([a.id,a.title])
    return JsonResponse({'data':list2})
def getArea2(request,pid):
    list = Areas.objects.filter(parea_id=pid)
    list2 = []
    for a in list:
        list2.append({'id':a.id,'title':a.title})
    return JsonResponse({'data':list2})
def html(request):
    return render(request,'booktest/HTMLEdit.html')
def htmlHandler(request):
    content = request.POST['content']
    test = Test()
    test.content = content
    test.save()
    return HttpResponse('ok')
def html2(request):
    content = Test.objects.filter(pk=3)
    context = {'content':content}
    return render(request,'booktest/HTMLContent.html',context)

from django.views.decorators.cache import cache_page
from django.core.cache import cache

# @cache_page(60*10)
def cache1(request):
    # return HttpResponse("longk")
    # return HttpResponse("hello")
    # cache.set('key1','val1',500)
    # print(cache.get('key1'))
    cache.clear()
    # return render(request,'booktest/cache.html')
    return HttpResponse('ok')
def mysearch(request):
    return render(request,'booktest/mysearch.html')

from .task import *
#python manage.py celery worker --loglevel=info
def last(request):
    # sayhello()
    sayhello.delay()
    return HttpResponse('OK')
