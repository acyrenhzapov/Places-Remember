from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView

from places.forms import PlaceCreationForm
from places.models import Place
import json

class PlaceDetailView(DetailView):
    template_name = 'place.html'
    model = Place


class PlaceCreateView(LoginRequiredMixin, CreateView):
    form_class = PlaceCreationForm
    success_url = reverse_lazy('home')
    template_name = 'create_place.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form.data['location'])
        print(json.loads(form.data['location']))
        print(type(json.loads(form.data['location'])))
        # form.data['location']['coordinates'] = form.data['location']['coordinates'][::-1]
        return super().form_valid(form)


class MarkersMapView(TemplateView):
    """Markers map view."""
    template_name = "map.html"
