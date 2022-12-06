from django.contrib.gis.geos import Point
from django.test import TestCase, Client

from impressions.models import Impression
from users.models import CustomUser


# Create your tests here.


class ImpressionDetailViewTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser',
                                                   password='asuf234bk',
                                                   is_active=True,
                                                   is_staff=False,
                                                   is_superuser=False)

        self.another_user = CustomUser.objects.create_user(username='another_user',
                                                           password='another_user_password',
                                                           is_active=True,
                                                           is_staff=False,
                                                           is_superuser=False)
        self.client.login(username='testuser', password='asuf234bk')

    def test_no_impressions(self):
        """Check view return zero impressions for user that doesn't have any place"""
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "У вас нет ни одного воспоминания")

    def test_new_impression(self):
        """Check view return same impressions as user have"""
        place = self.create_impression("30's dormitory", "Okay", self.user, x=156.13123212, y=12.234234)
        response = self.client.get('/home/')
        self.assertQuerysetEqual(
            response.context['user'].place_set.all(),
            [place],
        )

    def test_no_impression_another_user(self):
        """
        Check user can't get impression of another user
        """
        self.create_impression("30's dormitory", "Okay", self.user, x=156.13123212, y=12.234234)
        self.client.logout()
        self.client.login(username='another_user', password='another_user_password')
        response = self.client.get('/place/1/')
        self.assertEqual(response.status_code, 404)

    def test_model_validation(self):
        pass
        # self.assertRaises(ValidationError, self.create_place, "30's dormitory", "Okay", self.user, x=180.1, y=12)
        # self.assertRaises(ValidationError, self.create_place, "30's dormitory", "Okay", self.user, x=156, y=90.1)
        # self.assertRaises(IntegrityError, self.create_place, None, "Okay", self.user, x=156, y=45)
        # self.assertRaises(IntegrityError, self.create_place, "30's dormitory", None, self.user, x=156, y=45)
        # self.assertRaises(IntegrityError, self.create_place, "30's dormitory", "Okay", None, x=156, y=45)

    @staticmethod
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
