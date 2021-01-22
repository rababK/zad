from rest_framework import serializers

from .models import AD ,comment

class AD_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AD
        fields = ('Ad_title', 'AdType', 'AdDetails','photo')

class comment_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = comment
        fields = ('user','post','comment_text',)

