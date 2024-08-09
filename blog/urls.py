from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users import views as users_views

# Mapeamento das URLs com a View
urlpatterns = [
  path('', views.home, name = 'blog-home'),
  path('about/', views.about, name = "blog-about"),
]