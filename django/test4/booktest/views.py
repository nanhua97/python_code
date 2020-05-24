#-*-coding:utf8-*-
from django.shortcuts import render,redirect
from .models  import *
from django.http import HttpResponse

def index(request):
    hero = HeroInfo.objects.get(pk=3)
    list = HeroInfo.objects.all()
    context = {'hero':hero,'list':list}
    return render(request,'booktest/index.html',context)
def show(request,id,id1):
    context = {'id':id,'id1':id1}
    return render(request,'booktest/show.html',context)
def base(request):
    return render(request,'booktest/base2.html')

def user(request):
    return render(request,'booktest/mall_user.html')
def user1(request):
    head = 'welcome to the world'
    context = {'head':head}
    return render(request,'booktest/mall_user1.html',context)
def htmlTest(request):
    html = '<h1>hello</h1>'
    context = {'h1':html}
    return render(request,'booktest/htmlTest.html',context)
def csrf1(request):
    return render(request,'booktest/csrf1.html')
def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)

from PIL import Image,ImageFilter,ImageFont,ImageDraw
import random
import io
def rndChar():
    return chr(random.randint(65,90))
def rndcolor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndcolor2():
    return (random.randint(37,255),random.randint(37,255),random.randint(37,255))
def gene_line(draw,width,height):
    begin = (random.randint(0,width),random.randint(0,height))
    end = (random.randint(0,width),random.randint(0,height))
    draw.line([begin,end],fill=rndcolor())
def gene_point(draw,width,height):
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rndcolor())
def gene_code(size,char):
    width,height=size
    image = Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('FreeMono.ttf',25)
    draw = ImageDraw.Draw(image)
    for i in char:
        draw.text((30*char.index(i),2),i,font=font,fill=rndcolor2())
    image = image.filter(ImageFilter.BLUR)
    return image
def change(request):
    width,height=(100,30)
    char=''
    for i in range(4):
        char = char+rndChar()
    request.session['code'] = char
    image = Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('FreeMono.ttf',25)
    draw = ImageDraw.Draw(image)
    for i in char:
        draw.text((20*char.index(i),2),i,font=font,fill=(0,0,0))
        # draw.text((30*char.index(i),2),i,font=font,fill=rndcolor2())
    # image = image.filter(ImageFilter.BLUR)
    image.save('./templates/booktest/code.png')
def changeCode(request):
    return redirect('/code1')
def code1(request):
    change(request)
    return render(request,'booktest/code1.html')
def code2(request):
    if request.session['code'].lower() == request.POST['uname'].lower():
        return HttpResponse('ok')
    else:
        return redirect('/code1')
    # return HttpResponse(request.session['code'])
# Create your views here.
