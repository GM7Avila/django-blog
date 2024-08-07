from django.urls import path
from . import views

# Mapeamento das URLs com a View
urlpatterns = [
  path('', views.home, name = 'blog-home'),
  path('about/', views.about, name = "blog-about"),
]