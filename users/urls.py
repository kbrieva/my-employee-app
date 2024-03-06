from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    path('', views.index, name="index")  ,
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
