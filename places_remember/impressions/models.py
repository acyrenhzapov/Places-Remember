from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.db.models import CharField
from django.urls import reverse
from users.models import CustomUser

from .validators import long_lat_validator

DEFAULT_POINT_COORDINATES = {
    # coordinates of Krasnoyarsk
    'x': 56.01416977236943,
    'y': 92.85782247644305,
}


class Impression(models.Model):
    """
    Impression about some location
    Attributes:
        title (CharField): Title of description
        description (TextField): Description of some location
        location (PointField): Coordinates of location
        user (CustomUser): User that create this impression
    """

    title = models.CharField(
        max_length=50,
        blank=False,
    )
    description = models.TextField(
        blank=True,
        default='',
    )
    location = models.PointField(
        default=Point(**DEFAULT_POINT_COORDINATES),
        validators=[long_lat_validator],
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='impressions',
    )

    def __str__(self) -> CharField:
        return self.title


