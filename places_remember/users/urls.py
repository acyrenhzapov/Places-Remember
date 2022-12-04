from django.urls import path

from .views import CustomUserSignUp, CustomUserLoginView, CustomUserLogoutView
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
