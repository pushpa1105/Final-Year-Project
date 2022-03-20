from django.shortcuts import render
from django.http import HttpResponse
from . models import information
#Create your views here.

def new(request):
    print("hello")
    #newsObj = information.objects.all()
    #print("hello")
    #context = {'newsObj':newsObj}
    #return render(request,'main/news.html')
    return HttpResponse(request, "Hello") 
    
