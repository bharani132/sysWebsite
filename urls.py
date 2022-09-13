from django.contrib import admin
from django.urls import path,include
from . import views
from .views import index,index1,about,service,team,portfolio,contact

urlpatterns = [
    path('',views.index),
    path('index',views.index1),
    path('about',views.about),
    path('service',views.service),
    path('team',views.team),
    path('portfolio',views.portfolio),
    path('contact',views.contact)
]