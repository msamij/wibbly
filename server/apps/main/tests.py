from django.test import Client, TestCase
from django.urls import resolve

from server.apps.hotels.models import Hotel
from .views import index, get_hotel_data


class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_returns_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_function_returns_hotel_objects(self):
        self.client.get('/')
