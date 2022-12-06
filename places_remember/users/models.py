from django.contrib.auth.models import AbstractUser
from django.db.models import TextField


class CustomUser(AbstractUser):
    """
    User that can add impressions

    Attributes:
    -----------------
    avatar: url to profile picture
    social_backend: name of backend via user auth
    """
    avatar = TextField(default='')
    backend_name = TextField(default='')
