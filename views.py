from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.apps import apps
from .models import info

# Create your views here.
my_info = info.objects.all()

def index(request):
    if request.method== 'GET':
        return render(request,'index.html',{'infos':my_info})
def index1(request):
    return render(request,'index.html',{'infos':my_info})
def about(request):
    return render(request,'about.html',{'infos':my_info})
def service(request):
    return render(request,'service.html',{'infos':my_info})
def team(request):
    return render(request,'team.html',{'infos':my_info})
def portfolio(request):
    return render(request,'portfolio.html',{'infos':my_info})
def contact(request):
    return render(request,'contact.html',{'infos':my_info})