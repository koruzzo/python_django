from os import path
from django.contrib import admin
from django.urls import path
from api.views import EndPointDWH

urlpatterns = [
    path('',EndPointDWH.as_view())
]
