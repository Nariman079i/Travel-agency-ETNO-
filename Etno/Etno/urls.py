
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from Etno import settings

urlpatterns = [
    path('site/administration/qwerty654321/userroot/', admin.site.urls),
    path('',include('ture.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)