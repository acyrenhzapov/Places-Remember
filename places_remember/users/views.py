from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class CustomUserLogoutView(LogoutView):
    """
    View to logout
    """
    success_url = reverse_lazy('home')
