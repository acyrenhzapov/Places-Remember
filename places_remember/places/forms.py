from django.forms import ModelForm
from leaflet.forms.widgets import LeafletWidget
from leaflet.forms.fields import PointField
from places.models import Place

# from django.contrib.gis import forms
LEAFLET_WIDGET_ATTRS = {
    'map_height': '600px',
    'map_width': '50%',
    'display_raw': 'true',
    'map_srid': 4326,
}


class PlaceCreationForm(ModelForm):
    location = PointField(widget=LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS))

    class Meta:
        model = Place
        fields = ('title', 'description', 'location')
        widgets = {'location': LeafletWidget()}
