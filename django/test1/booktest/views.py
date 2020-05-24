from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import *


def index(request):
    #temp = loader.get_template('booktest/index.html')
    #return HttpResponse(temp.render())
    #context = {'title':'First Page'}
    bookList = BookInfo.objects.all()
    context = {'title':bookList}
    return render(request,'booktest/index.html',context)
# Create your views here.
def show(request,id):
    book = BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    context = {'book':herolist}
    return render(request,'booktest/show.html',context)
