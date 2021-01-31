from rest_framework import serializers

from django.apps import apps
AD = apps.get_model('zad', 'AD')

class AD_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AD
        fields = ['Ad_title','Ad_details','photo','term','user','category','approved','valid','created_at','update_at','publish_date']
        read_only_fields = ['id', 'user','valid','created_at','update_at','publish_date','approved']

