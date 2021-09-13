from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostArticle),
    path('<int:num>/', views.article),
    path('<int:num>/edit/', views.EditArticle),
]