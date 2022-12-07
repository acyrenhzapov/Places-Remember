from django.contrib.gis.geos import Point
from django.test import Client, TestCase
from django.urls import reverse

from users.models import CustomUser
from ..factories import ImpressionFactory
from ..models import Impression


def create_impression(
        title: str,
        description: str,
        user: CustomUser,
        x: float,
        y: float, ) -> Impression:
    """
    Create impression in db to test some functions
    """
    impression = Impression.objects.create(title=title,
                                           description=description,
                                           user=user,
                                           location=Point(x=x,
                                                          y=y))
    impression.full_clean()
    return impression


class ImpressionDetailViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user_data = {
            'username': 'testuser',
            'password': 'asuf234bk,'
        }
        self.another_user_data = {
            'username': 'another_user',
            'password': 'another_user_password',
        }
        self.user = CustomUser.objects.create_user(
            **self.user_data,
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )

        self.another_user = CustomUser.objects.create_user(
            **self.another_user_data,
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )
        self.client.login(**self.user_data)

    def test_no_impressions(self):
        """Check view return zero impressions for user that doesn't have any place"""
        response = self.client.get('/home/')
        self.assertContains(response, "У вас нет ни одного воспоминания")

    def test_new_impression(self):
        """Check view return same impressions as user have"""
        place = ImpressionFactory(user=self.user)
        ImpressionFactory(user=self.another_user)
        response = self.client.get('/home/')
        self.assertQuerysetEqual(
            response.context['user'].impressions.all(),
            [place],
        )

    def test_no_impression_another_user(self):
        """
        Check user can't get impression of another user
        """
        create_impression("30's dormitory", "Okay", self.user, x=156.13123212, y=12.234234)
        self.client.logout()
        self.client.login(**self.another_user_data)
        response = self.client.get(reverse('impressions:impression-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 404)
