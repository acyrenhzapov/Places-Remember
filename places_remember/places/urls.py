from django.urls import path
from places.views import PlaceCreateView, PlaceDetailView

app_name = 'places'
urlpatterns = [
    path('<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
    path('', PlaceCreateView.as_view(), name='create'),
]
