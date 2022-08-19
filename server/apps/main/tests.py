from urllib import response
from django.test import Client, TransactionTestCase
from server.apps.hotels.models import Hotel


class HomePageTest(TransactionTestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('/')

    def test_home_page_returns_correct_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'index.html')

    def test_template_contains_correct_context(self):
        self.assertCountEqual(
            self.response.context['hotels'], Hotel.objects.all()[:4])
