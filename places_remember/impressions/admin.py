from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from .models import Impression

# admin.site.register(
#     Impression,
#     LeafletGeoAdmin,
#     settings_overrides={
#         'DEFAULT_CENTER': (59.334591, 18.063240),
#         'DEFAULT_ZOOM': 10,
#         'TILES': [('', '//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', '')],
#     }
# )

@admin.register(Impression)
class MarkerAdmin(LeafletGeoAdmin):
    """Marker admin."""

    list_display = ("title", "location")
