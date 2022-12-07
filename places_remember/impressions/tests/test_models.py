from django.test import TestCase

from ..factories import ImpressionFactory


class ImpressionTestCase(TestCase):
    def setUp(self) -> None:
        self.impression = ImpressionFactory()

    def test_str_impression(self):
        """Check """
        self.assertEqual(str(self.impression), "IKIT0")
