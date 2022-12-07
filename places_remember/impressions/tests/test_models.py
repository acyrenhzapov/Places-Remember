from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase, Client

from users.models import CustomUser
from .base_functionality import create_impression
from ..models import Impression


class ImpressionTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser',
                                                   password='asuf234bk',
                                                   is_active=True,
                                                   is_staff=False,
                                                   is_superuser=False)
        impression = Impression.objects.create(title="30's dormitory", description="Okay", user=self.user, location=Point(x=60, y=3))
        self.impression_pk = impression.pk

    def test_model_validation(self):
        """Check valid parameters"""
        self.assertRaises(ValidationError, create_impression, "30's dormitory", "Okay", self.user, x=180.1, y=12)
        self.assertRaises(ValidationError, create_impression, "30's dormitory", "Okay", self.user, x=156, y=90.1)

    def test_title_label(self):
        impression = Impression.objects.get(id=self.impression_pk)
        field_label = impression._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_label(self):
        impression = Impression.objects.get(id=self.impression_pk)
        field_label = impression._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_title_max_length(self):
        impression = Impression.objects.get(id=self.impression_pk)
        max_length = impression._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_str_impression(self):
        impression = Impression.objects.get(id=self.impression_pk)
        self.assertEqual(str(impression), "30's dormitory")

    def test_get_absolute_url(self):
        impression = Impression.objects.get(id=self.impression_pk)
        self.assertEqual(impression.get_absolute_url(), f'/impressions/{self.impression_pk}/')

