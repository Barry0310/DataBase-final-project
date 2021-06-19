from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostArticle),
    path('<int:num>/', views.article),
]