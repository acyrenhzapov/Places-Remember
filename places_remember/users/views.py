# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from places_remember import settings
from .forms import CustomUserCreationForm, CustomUserLoginForm


class CustomUserSignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class CustomUserLoginView(LoginView):
    form_class = CustomUserLoginForm
    success_url = reverse_lazy('home')
    template_name = 'login.html'


class LogoutView(View):

    @staticmethod
    def get(request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class CustomUserLogoutView(LoginView):
    form_class = CustomUserLoginForm
    success_url = reverse_lazy('home')
