import factory
from django.contrib.gis.geos import Point
from users.factories import CustomUserFactory

from .models import Impression


class ImpressionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Impression

    title = factory.Sequence(lambda n: 'IKIT%d' % n)
    description = "My university"
    location = Point(
        x=55.99440809433912,
        y=92.79722994760965,
    )
    user = factory.SubFactory(CustomUserFactory)
