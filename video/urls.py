from django.urls import path, include
from . import views


urlpatterns = [
    path('video', views.video, name='video'),
    ]