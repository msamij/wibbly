from server.apps.main.utils.context_objects import *

from test_setup import HomePageTestSetup


class HomePageActivityContextTest(HomePageTestSetup):
    def setUp(self):
        super().setUp()

    def test_template_contains_correct_activity_context(self):
        self.assertEqual(
            self.response.context['activities'], get_activity_with_images())


class HomePageHotelContextTest(HomePageTestSetup):
    def setUp(self):
        super().setUp()

    def test_template_contains_correct_hotel_context(self):
        self.assertEqual(
            self.response.context['hotels'], get_hotel_with_images())


class HomePageTourContextTest(HomePageTestSetup):
    def setUp(self):
        super().setUp()

    def test_template_contains_correct_tour_context(self):
        self.assertEqual(
            self.response.context['tours'], get_tour_with_images())
