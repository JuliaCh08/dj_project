from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_view, name='articles_home'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='article-detail')
    ]