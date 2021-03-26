from django.conf.urls import url
from django.contrib import auth
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

app_name = "registration"

urlpatterns = [
    path('', views.home, name='home'),


    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/<str:email>/', views.profile, name='profile'),
]
