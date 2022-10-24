from django.contrib import admin
from django.urls import path, include 
from .views import *

urlpatterns = [
    path('new/', get_api, name="view"),
   

]
