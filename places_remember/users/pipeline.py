from django.shortcuts import redirect


def get_avatar(backend, response, user=None, *args, **kwargs):
    def save_avatar(response_name: str):
        url = response.get(response_name, '')
        if url:
            user.avatar = url
            user.save()

    if backend.name == 'vk-oauth2':
        save_avatar('photo')
    elif backend.name == "google-oauth2":
        save_avatar('picture')


def auth_allowed(backend, details, response, *args, **kwargs):
    if not backend.auth_allowed(response, details):
        return redirect('user:error')
