
from django.urls import include, path
from django.contrib.admin import AdminSite
from django.contrib import admin
from django.conf.urls import url, include
#from mysite.zad_app import views
admin.autodiscover()
#from.import settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('zad/', include('zad.urls')),
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    ]
#urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)