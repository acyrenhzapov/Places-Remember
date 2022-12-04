from django.forms import ModelForm
from leaflet.forms.fields import PointField
from leaflet.forms.widgets import LeafletWidget

from places.models import Place

LEAFLET_WIDGET_ATTRS = {
    'map_height': '200%',
    'map_width': '200%',
    'map_srid': 4326,
}


class PlaceCreationForm(ModelForm):
    location = PointField(widget=LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS))

    class Meta:
        model = Place
        fields = ('title',
                  'description',
                  'location')
        widgets = {'location': LeafletWidget()}
