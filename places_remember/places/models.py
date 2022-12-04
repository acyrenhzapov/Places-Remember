from django.contrib.gis.geos import Point
from django.contrib.gis.db import models
from django.urls import reverse

from users.models import CustomUser


class Place(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.PointField(default=Point(x=56.01416977236943, y=92.85782247644305))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("place:place_detail", args=[self.pk])
