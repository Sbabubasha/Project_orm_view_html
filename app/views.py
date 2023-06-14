from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *

def data_insertion(request):
    tn=input('enter the topic_name: ')
    Ts=Topic.objects.get_or_create(topic_name=tn)[0]
    Ts.save()
    return HttpResponse('data insertion in Topic is successfull')

def webpage_insertion(request):
    tn=input('enter the topic_name: ')
    na=input('enter the name: ')
    ur=input('enter the url_name: ')
    Ts=Topic.objects.get_or_create(topic_name=tn)[0]
    Ts.save()
    web=Webpage.objects.get_or_create(topic_name=Ts,name=na,url=ur)[0]
    web.save()
    return HttpResponse('Webpage insertion is successfull...!')
def access_insert(request):
    tn=input('enter the topic_name: ')
    na=input('enter the name: ')
    ur=input('enter the url_name: ')
    Ts=Topic.objects.get_or_create(topic_name=tn)[0]
    Ts.save()
    web=Webpage.objects.get_or_create(topic_name=Ts,name=na,url=ur)[0]
    web.save()
    a=input('enter the author: ')
    te=input('enter the date: ')
    ac=Accessrecords.objects.get_or_create(name=web,author=a,date=te)[0]
    ac.save()
    return HttpResponse('Webpage insertion is successfull...!')



def front(request):
    #LOT=Topic.objects.all()
    LOT=Topic.objects.filter(topic_name='Cricket')
    
    #LOT=Topic.objects.order_by('-topic_name')
    #tp=Topic.objects.get_or_create(topic_name='FootBall')[0]
    #tp.save()
    #Topic.objects.update_or_create(defaults={'topic-name':tp})
    #Topic.objects.filter('football').delete()
    d={'topics':LOT}
    return render(request,"front.html",d)

def display_web(request):
    low=Webpage.objects.all()
    #low=Webpage.objects.order_by('name')
    #Webpage.objects.filter(name='MahendraSingDhoni').update(url='http//:MahendraSingDhon.com')
    #tw=Topic.objects.get_or_create(topic_name='football')[0]
    #tw.save()
    #Webpage.objects.update_or_create(name='mesey',defaults={'topic_name':tw,'url':'http://mesey.com'})
    #Webpage.objects.filter(name='mesey').delete()
    d={'web':low}

    return render(request,'display_web.html',d)

def display_access(request):
    #loa=Accessrecords.objects.all()
    #loa=Accessrecords.objects.filter(author='msd')
    loa=Accessrecords.objects.order_by('name')
    d={'access':loa}
    return render(request,'display_access.html',d)