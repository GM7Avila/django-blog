from django.urls import path
from . import views
from users import views as users_views

# Mapeamento das URLs com a View
urlpatterns = [
  path('', views.home, name = 'blog-home'),
  path('about/', views.about, name = "blog-about"),
  path('signup/', users_views.register, name = 'register'),
]