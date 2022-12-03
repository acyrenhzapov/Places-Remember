from django.contrib.gis.geos import Point
from django.contrib.gis.db import models
from django.urls import reverse

from users.models import CustomUser

LEAFLET_WIDGET_ATTRS = {
    'map_height': '600px',
    'map_width': '50%',
    'display_raw': 'true',
    'map_srid': 4326,
}


# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.PointField(default=Point(y=56.01416977236943, x=92.85782247644305))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("place:place_detail", args=[self.pk])
