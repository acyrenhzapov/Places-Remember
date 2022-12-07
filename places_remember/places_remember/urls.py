from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from places_remember.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('users/', include('users.urls'), name='users'),
    path('impressions/', include('impressions.urls'), name='impressions'),
    path('', RedirectView.as_view(url='/home')),
]
