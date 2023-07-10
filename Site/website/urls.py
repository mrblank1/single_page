from django.contrib import admin
from django.urls import path
from website.views import *
# from django.urls import include
urlpatterns = [
    path('',home , name='home')
]
