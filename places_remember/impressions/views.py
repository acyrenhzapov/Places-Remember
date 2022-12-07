from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from impressions.forms import ImpressionCreationForm
from impressions.models import Impression


class ImpressionDetailView(DetailView):
    """
    View with information about impression
    """
    template_name = 'impression.html'
    model = Impression

    def get_object(self, queryset=None) -> Impression:
        """Check that this impression was created by current user
        Returns:
            Impression class or raise Http404(Exception)
        """
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

    def form_valid(self, form) -> HttpResponseRedirect:
        """
        Link impression with user
        Args:
            form: form with full information but user
        Returns:
            form with full information about place
        """
        form.instance.user = self.request.user
        return super().form_valid(form)
