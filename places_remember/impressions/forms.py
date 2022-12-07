from django.forms import ModelForm
from leaflet.forms.fields import PointField
from leaflet.forms.widgets import LeafletWidget

from impressions.models import Impression

LEAFLET_WIDGET_ATTRS = {
    'map_height': '200%',
    'map_width': '200%',
    'map_srid': 4326,
}


class ImpressionCreationForm(ModelForm):
    """
    Form to create instance of Impression class
    """
    location = PointField(widget=LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS))

    class Meta:
        model = Impression
        fields = ('title',
                  'description',
                  'location')
        widgets = {'location': LeafletWidget()}
