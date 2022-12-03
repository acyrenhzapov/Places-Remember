from django.urls import path

from .views import CustomUserSignUp, CustomUserLoginView, CustomUserLogoutView

urlpatterns = [
    path('signup/', CustomUserSignUp.as_view(), name='signup'),
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('logout/', CustomUserLogoutView.as_view(), name='logout'),
]
