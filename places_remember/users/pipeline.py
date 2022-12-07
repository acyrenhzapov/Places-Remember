from social_core.exceptions import AuthForbidden

from users.models import CustomUser


def get_avatar(backend, response, user: CustomUser = None, *args, **kwargs):
    def save_avatar(response_name: str):
        url = response.get(response_name, '')
        if url:
            user.avatar = url
            user.save()

    if backend.name == 'vk-oauth2':
        save_avatar('photo')
    elif backend.name == "google-oauth2":
        save_avatar('picture')


def email_required(backend, response, user: CustomUser = None, *args, **kwargs):
    if not (response.get('email') or user and user.email):
        raise AuthForbidden(backend)


def get_backend_name(backend, response, user: CustomUser = None, *args, **kwargs):
    user.backend_name = backend.name
    user.save()
