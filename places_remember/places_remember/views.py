from django.views.generic import DetailView

from users.models import CustomUser


class HomeView(DetailView):
    template_name = 'home.html'
    model = CustomUser

    def get_object(self):
        return self.request.user


