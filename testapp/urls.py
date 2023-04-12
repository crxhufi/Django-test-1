from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('log_out/', views.log_out, name="log_out")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)