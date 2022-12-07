from django.views.generic import DetailView

from users.models import CustomUser


class HomeView(DetailView):
    template_name = 'home.html'
    model = CustomUser

    def get_object(self):
        """Return CustomUser instance to check is user authorized or not"""
        return self.request.user
