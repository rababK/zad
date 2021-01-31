
from django.urls import path
from django.contrib import admin
from django.conf.urls import include
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
   path('admin/', admin.site.urls),
   path('zad/', include('zad.urls')),
   path('api/', include('api.urls')),
   path('registration/', include('registration.urls')),
   path('', include('django.contrib.auth.urls')),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # ...
    prefix_default_language=False
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

