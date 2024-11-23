from django.urls import path
from .views import user_signup
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('signup', user_signup, name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset')
]