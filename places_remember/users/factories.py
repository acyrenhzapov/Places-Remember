import factory

from .models import CustomUser


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Sequence(lambda n: 'JohnDoe%d' % n)
    first_name = "John"
    last_name = "Doe"
    password = factory.PostGenerationMethodCall(
        'set_password',
        'mysecret',
    )
    email = factory.Sequence(lambda n: 'JohnDoe%d@gmail.com' % n)
