from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view , name="home")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
