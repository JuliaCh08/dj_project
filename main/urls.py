from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>', views.DogBreedDetailView.as_view(), name='dog_breed'),
    path('Privacy_policy', views.policy, name='policy'),
    ]

