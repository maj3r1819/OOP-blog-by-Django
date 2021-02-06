from django.urls import path
from . import views   # . means current directory
urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about')
]