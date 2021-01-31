from rest_framework.response import Response
from rest_framework import generics, mixins

from .serializers import AD_Serializer
from django.apps import apps
AD = apps.get_model('zad', 'AD')



class AdRUDApi(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView

    serializer_class        = AD_Serializer

    def get_queryset(self):
        return AD.objects.all()


    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class AdCLApi(mixins.CreateModelMixin, generics.ListAPIView): # DetailView CreateView FormView

    serializer_class        = AD_Serializer
    queryset                = AD.objects.all()


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
