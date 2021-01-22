from rest_framework.response import Response

from .serializers import AD_Serializer,comment_Serializer
from .models import AD, comment
from rest_framework.decorators import api_view

@api_view(['GET',])
def AD_list(request):
    ADS = AD.objects.all()
    data = AD_Serializer(ADS,many=True).data
    return Response({"data":data})
