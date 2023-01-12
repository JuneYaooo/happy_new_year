from django.urls import path
from .views import generate_painting
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('new_year_paintings/', generate_painting, name='generate_painting'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)