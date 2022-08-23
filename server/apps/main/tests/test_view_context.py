from server.apps.main.utils import *

from test_setup import HomePageTestSetup


class HomePageActivityContextTest(HomePageTestSetup):
    def setUp(self):
        super().setUp()
        self.activity = create_activity_test_object()

    def test_template_contains_correct_activity_context(self):
        self.assertQuerysetEqual(
            self.response.context['activities'], [self.activity])
        self.assertQuerysetEqual(self.response.context['activity_images'],
                                 [create_activity_image_test_object(self.activity)])


class HomePageHotelContextTest(HomePageTestSetup):
    def setUp(self):
        super().setUp()
        self.hotel = create_hotel_test_object()

    def test_template_contains_correct_hotel_context(self):
        self.assertQuerysetEqual(self.response.context['hotels'], [self.hotel])
        self.assertQuerysetEqual(self.response.context['hotel_images'],
                                 [create_hotel_image_test_object(self.hotel)])


class HomePageTourContextTest(HomePageTestSetup):
    def setUp(self):
        super().setUp()
        self.tour = create_tour_test_object()

    def test_template_contains_correct_tour_context(self):
        self.assertQuerysetEqual(self.response.context['tours'], [self.tour])
        self.assertQuerysetEqual(self.response.context['tour_images'],
                                 [create_tour_image_test_object(self.tour)])
