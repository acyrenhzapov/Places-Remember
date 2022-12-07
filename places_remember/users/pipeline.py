"""
This module need to customize auth pipeline in social-auth-app-django
Add some features or change some logic
"""
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import AuthForbidden
from users.models import CustomUser


def get_avatar(backend: BaseOAuth2, response: dict, user: CustomUser = None, *args, **kwargs) -> None:
    """
    Update profile pic of CustomUser when he/she auth/login
    Attributes:
        backend: Social core backend via user auth (GoogleOAuth2, VkOAuth2)
        response: dict with information about auth
        user: User that currently auth or login
    Returns:
        None
    """
    def save_avatar(response_name: str):
        url = response.get(response_name, '')
        if url:
            user.avatar = url
            user.save()
    if backend.name == 'vk-oauth2':
        save_avatar('photo')
    elif backend.name == "google-oauth2":
        save_avatar('picture')


def email_required(backend: BaseOAuth2, response: dict, user: CustomUser = None, *args, **kwargs):
    """
    Check that response or user contain email to link it further with CustomUser model in db
    Attributes:
        backend: Social core backend via user auth (GoogleOAuth2, VkOAuth2)
        response: dict with information about auth
        user: User that currently auth or login
    Returns:
        None
    """
    if not (response.get('email') or user and user.email):
        raise AuthForbidden(backend)


def get_backend_name(backend: BaseOAuth2, response: dict, user: CustomUser = None, *args, **kwargs):
    """
    Save information through which backend the user auth
    Attributes:
        backend: Social core backend via user auth (GoogleOAuth2, VkOAuth2)
        response: dict with information about auth
        user: User that currently auth or login
    Returns:
        None
    """
    user.backend_name = backend.name
    user.save()
