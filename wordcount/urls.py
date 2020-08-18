from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('countss/', views.count, name='count'),
    path('abouts/', views.about, name='about')
]
