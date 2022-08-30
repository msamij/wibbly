from django.test import TestCase, Client
from .utils.context_objects import *


def create_test_tour_object():
    return Tour.objects.create(tour_name='test_tour', tour_price=0, tour_description='', max_participants=0, tour_duration=0)


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
        self.tour_name = 'test_tour'

        self.assertEqual(
            self.response.context['tour_name'], get_tour_name(self.tour_name))
        self.assertEqual(
            self.response.context['tour_price'], get_tour_price(self.tour_name))
        self.assertEqual(
            self.response.context['tour_description'], get_tour_description(self.tour_name))
        self.assertEqual(
            self.response.context['max_participants'], get_tour_max_participants(self.tour_name))
        self.assertEqual(
            self.response.context['tour_duration'], get_tour_duration(self.tour_name))
        # self.assertEqual(
        #     self.response.context['tour_rating'], get_tour_rating(self.response.context['tour']))
        # self.assertEqual(self.response.context['tour_images'], get_tour_images(
        #     self.response.context['tour']))
        # self.assertEqual(self.response.context['tour_instructor'], get_tour_instructor(
        #     self.response.context['tour']))
