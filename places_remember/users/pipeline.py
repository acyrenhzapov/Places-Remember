from django.shortcuts import redirect


def get_avatar(backend, response, user=None, *args, **kwargs):
    url = None

    if backend.name == 'vk-oauth2':
        url = response.get('photo', '')

    if url:
        user.avatar = url
        user.save()
        print(user.avatar)


def auth_allowed(backend, details, response, *args, **kwargs):
    if not backend.auth_allowed(response, details):
        return redirect('user:error')
