# Create your views here.
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, CustomUserLoginForm


class CustomUserSignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CustomUserLoginView(LoginView):
    form_class = CustomUserLoginForm
    success_url = reverse_lazy('home')
    template_name = 'login.html'


class CustomUserLogoutView(LoginView):
    form_class = CustomUserLoginForm
    success_url = reverse_lazy('login')
    template_name = 'login.html'
