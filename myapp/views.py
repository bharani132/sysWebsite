from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.apps import apps

# Create your views here.
def index(request):
    return render(request,'index.html')