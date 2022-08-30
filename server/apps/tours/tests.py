from django.test import TestCase, Client
from .utils.context_objects import TourContext
from .utils.test_objects import create_test_tour_object


class TourPageTest(TestCase):
    def setUp(self):
        super().setUp()
        self.client = Client()
        self.tour = create_test_tour_object()
        self.response = self.client.get('/tours/test_tour')

    def test_tour_page_returns_correct_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'tour.html')

    def test_tour_page_contains_correct_context(self):
        self.tour_context_obj = TourContext('test_tour')

        self.assertEqual(
            self.response.context['tour_name'], self.tour_context_obj.get_tour_name())
        self.assertEqual(
            self.response.context['tour_price'], self.tour_context_obj.get_tour_price())
        self.assertEqual(
            self.response.context['tour_description'], self.tour_context_obj.get_tour_description())
        self.assertEqual(
            self.response.context['max_participants'], self.tour_context_obj.get_tour_max_participants())
        self.assertEqual(
            self.response.context['tour_duration'], self.tour_context_obj.get_tour_duration())
        self.assertEqual(
            self.response.context['tour_rating'], self.tour_context_obj.get_tour_rating())
        self.assertEqual(
            self.response.context['tour_images'], self.tour_context_obj.get_tour_images())
        self.assertEqual(
            self.response.context['tour_instructor'], self.tour_context_obj.get_tour_instructor())
