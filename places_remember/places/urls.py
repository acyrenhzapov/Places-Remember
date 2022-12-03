from django.urls import path
from places.views import PlaceCreateView, MarkersMapView, PlaceDetailView

app_name = 'places'
urlpatterns = [
    path('<int:pk>/', PlaceDetailView.as_view(), name='place-detail'),
    path('create/', PlaceCreateView.as_view(), name='create'),
    path("map/", MarkersMapView.as_view())
]
