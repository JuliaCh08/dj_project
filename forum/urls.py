from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_view, name='forum'),
    path('questions', views.questions, name='forum-detail'),
    path('answers/<int:id>',  views.answer,  name='answer-detail'),
    ]

#/<int:id>

