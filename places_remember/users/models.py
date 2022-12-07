from django.contrib.auth.models import AbstractUser
from django.db.models import TextField, URLField


class CustomUser(AbstractUser):
    """
    Impression about some location
    Attributes:
        avatar (URLField): url to profile pic
        backend_name (TextField): backend name through which the user auth
    """
    avatar = URLField(default='')
    backend_name = TextField(default='google-oauth2')
