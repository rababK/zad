from django.urls import path
from . import views
from . import models
from django.conf.urls import url, include
from rest_framework import routers
from . import API

app_name = 'zad'
urlpatterns = {

    path('', views.home, name='home'),
    path('post_details/<int:pk>/', views.post_details, name='post_details'),

    path('Add_new_AD/', views.Add_new_AD, name='Add_new_AD'),
    path('Add_post/', views.Add_post, name='Add_post'),
    path('MyAd/', views.MyAd, name='MyAd'),
    path('Add_comment/<int:pk>/', views.Add_comment, name='Add_comment'),
    path('ContactUs/', views.ContactUs, name='ContactUs'),
    # ______________API________________
    path('api-auth/AD_list', API.AD_list, name=' AD_list'),

}
