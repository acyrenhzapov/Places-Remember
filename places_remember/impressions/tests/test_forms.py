from django.contrib.gis.geos import Point
from django.test import TestCase

from users.models import CustomUser
from ..forms import ImpressionCreationForm


class ImpressionCreationFormTestCase(TestCase):
    def setUp(self) -> None:
        self.user_data = {
            'username': 'testuser',
            'password': 'asuf234bk,'
        }
        self.user = CustomUser.objects.create_user(
            **self.user_data,
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )

    def test_empty_title(self):
        """Test that title shouldn't be empty"""
        form = ImpressionCreationForm(data={
            'title': '',
            'description': 'simple desc',
            'location': Point(x=0, y=0),
            'user': self.user,
        })
        self.assertEqual(
            form.errors["title"], ["This field is required."]
        )

    def test_no_point(self):
        """Test that location should be marked"""
        form = ImpressionCreationForm(data={
            'title': 'some title',
            'description': 'simple desc',
            'location': None,
            'user': self.user,
        })
        self.assertEqual(
            form.errors["location"], ["No geometry value provided."]
        )
