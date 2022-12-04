from django.contrib import admin
from django.urls import path, include
from places_remember.views import HomeView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('users/', include('users.urls'), name='users'),
    path('places/', include('places.urls'), name='places'),
    path('', RedirectView.as_view(url='/home')),\
]
