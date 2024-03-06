from django.urls import path
from django.conf import settings
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name="index"),
]
