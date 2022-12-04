from django.contrib.auth.models import AbstractUser
from django.db.models import TextField


class CustomUser(AbstractUser):
    avatar = TextField(default='')
