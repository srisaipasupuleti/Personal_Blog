from django.urls import path
from .views import user_signup, guest_login
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    path('signup', user_signup, name='signup'),
    path('guest_login', guest_login, name='guest_login'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset')
]