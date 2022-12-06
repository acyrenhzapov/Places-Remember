# Create your views here.
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class CustomUserLogoutView(LogoutView):
    success_url = reverse_lazy('home')
