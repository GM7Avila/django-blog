from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users import views as users_views

# Mapeamento das URLs com a View
urlpatterns = [
  path('', views.home, name = 'blog-home'),
  path('about/', views.about, name = "blog-about"),

  path('signup/', users_views.register, name = 'register'),
  path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
  path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
]