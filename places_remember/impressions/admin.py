from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Impression


@admin.register(Impression)
class MarkerAdmin(LeafletGeoAdmin):
    """
    Display Impressions in admin page
    """
    list_display = (
        "title",
        "user",
        "location",
    )
