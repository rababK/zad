from django.urls import path
from . import views
from . import models
from django.conf.urls import url, include
from rest_framework import routers

app_name = 'mysite.zad'
urlpatterns = [

    path('', views.home, name='home'),
    path('AD_details/<int:pk>/', views.AD_details, name='AD_details'),
    path('set_language/', views.set_language, name='set_language'),
    path('Add_new_AD/', views.Add_new_AD, name='Add_new_AD'),
    path('MyAd/', views.MyAd, name='MyAd'),
    path('like_Ad/<int:pk>/',views.like_Ad,name='like_Ad'),
    path('ContactUs/', views.ContactUs, name='ContactUs'),


]
