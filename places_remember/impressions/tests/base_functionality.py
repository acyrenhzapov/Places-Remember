from django.contrib.gis.geos import Point

from impressions.models import Impression
from users.models import CustomUser


def create_impression(title: str,
                      description: str,
                      user: CustomUser,
                      x: float,
                      y: float, ) -> Impression:
    impression = Impression.objects.create(title=title,
                                           description=description,
                                           user=user,
                                           location=Point(x=x,
                                                          y=y))
    impression.full_clean()
    return impression
