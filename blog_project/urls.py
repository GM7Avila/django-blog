from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as users_views

# Mapeamento das URLS dos apps
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', users_views.register, name = 'register'),
    path('profile/', users_views.profile, name = 'profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('', include('blog.urls')),
]
