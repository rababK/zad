from django.conf.urls import url
from django.urls import path
from . import views


app_name ='registration'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    path('profile/<str:email>/', views.profile, name='profile'),
]
