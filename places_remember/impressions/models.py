from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.urls import reverse

from users.models import CustomUser
from .validators import long_lat_validator

DEFAULT_POINT_COORDINATES = {
    'x': 56.01416977236943,
    'y': 92.85782247644305,
}


class Impression(models.Model):
    """
    User's impression about some location

    Attributes
    -----------------
    title: Name of location that users want to describe
    description: Some comment about location
    location: Coordinates of location
    user: User that create this impression
    """
    title = models.CharField(max_length=50,
                             blank=False, )
    description = models.TextField(blank=True,
                                   default='')
    location = models.PointField(default=Point(**DEFAULT_POINT_COORDINATES),
                                 validators=[long_lat_validator], )
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE, )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("impressions:impression_detail", args=[self.pk])
