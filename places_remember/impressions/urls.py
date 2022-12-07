from django.urls import path
from impressions.views import ImpressionCreateView, ImpressionDetailView

app_name = 'impressions'
urlpatterns = [
    path('<int:pk>/', ImpressionDetailView.as_view(), name='impression-detail'),
    path('', ImpressionCreateView.as_view(), name='create'),
]
