from django.urls import path
from . import API

app_name = 'zad'
urlpatterns = {

    # ______________API________________
    path('api-auth/', API.AD_list, name=' AD_list'),

}
