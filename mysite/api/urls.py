from django.urls import path


from .views import AdRUDApi, AdCLApi

urlpatterns = [
    path('', AdCLApi.as_view(), name='Ad c/l api'),
    path('<int:pk>/', AdRUDApi.as_view(), name='Ad RUD api'),
]