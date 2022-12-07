from django.views.generic import DetailView
from users.models import CustomUser


class HomeView(DetailView):
    """
    View where user can login, check all impressions or logout/disconnect
    """
    template_name = 'home.html'
    model = CustomUser

    def get_object(self, queryset=None):
        """
        Add current user to template to check inside it is user auth or not
        """
        return self.request.user
