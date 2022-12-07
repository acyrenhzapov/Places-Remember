from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView

from impressions.forms import ImpressionCreationForm
from impressions.models import Impression


class ImpressionDetailView(DetailView):
    """
    View with information about impression
    """
    template_name = 'impression.html'
    model = Impression

    def get_object(self, queryset=None):
        """Check that this impressions was created by current user"""
        obj = super().get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj


class ImpressionCreateView(LoginRequiredMixin, CreateView):
    """
    View to create some impression
    """
    form_class = ImpressionCreationForm
    success_url = reverse_lazy('home')
    template_name = 'create_impression.html'

    def form_valid(self, form):
        """
        Link impression with user
        :param form: form with full information but user
        :return: form with full information about place
        """
        form.instance.user = self.request.user
        return super().form_valid(form)
