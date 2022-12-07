from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django.forms import ModelForm
from impressions.models import Impression
from leaflet.forms.fields import PointField
from leaflet.forms.widgets import LeafletWidget

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
        fields = (
            'title',
            'description',
            'location',
        )
        widgets = {'location': LeafletWidget()}

    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('title', css_class='form-control mt-2 mb-3'),
        Field('description', rows="3", css_class='form-control mb-3'),
        Field('location', css_class='form-control w-0 mb-3'),
        Submit('submit', 'Submit'),
    )
