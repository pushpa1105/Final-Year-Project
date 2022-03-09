from django.shortcuts import render
from django.http import HttpResponse
from .models import information
# Create your views here.

def news(request):
    
    newsObj = information.objects.all()
    context = {'newsObj' : newsObj}

    return render(request, 'main/news.html', context)
