from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView

from places.forms import PlaceCreationForm
from places.models import Place


class PlaceDetailView(DetailView):
    template_name = 'place.html'
    model = Place

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super().get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj


class PlaceCreateView(LoginRequiredMixin, CreateView):
    form_class = PlaceCreationForm
    success_url = reverse_lazy('home')
    template_name = 'create_place.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
