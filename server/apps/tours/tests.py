from django.test import TestCase, Client
from .utils.context_objects import *


class TourPageTest(TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.response = self.client.get('/tours/<str:tour>')

    def test_tour_page_returns_correct_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'main.html')

    def test_tour_page_contains_correct_context(self):
        self.assertEqual(
            self.response.context['tour'], get_tour('test_tour'))
        self.assertEqual(
            self.response.context['tour_rating'], get_tour_rating(self.response.context['tour']))
        self.assertEqual(self.response.context['tour_images'], get_tour_images(
            self.response.context['tour']))
        self.assertEqual(self.response.context['tour_instructor'], get_tour_instructor(
            self.response.context['tour']))
