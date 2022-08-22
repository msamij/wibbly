from server.apps.main.utils import *

from test_setup import HomePageTestSetup


class HomePageActivityContextTest(HomePageTestSetup):
    def setUp(self):
        super().setUp()
        self.activity = create_activity_test_object(
            'Cycling', 100, 'Best activity')

    def test_template_contains_correct_activity_context(self):
        self.assertQuerysetEqual(
            self.response.context['activities'], [self.activity])

    def test_template_contains_activity_images(self):
        self.assertQuerysetEqual(self.response.context['activity_images'],
                                 [create_activity_image_test_object(self.activity, 'https://myimage.com/activityImage')])


class HomePageHotelContextTest(HomePageTestSetup):
    def setUp(self):
        super().setUp()
        self.hotel = create_hotel_test_object(
            'Transalvania', 100, 200, 'Best monster hotel')

    def test_template_contains_correct_hotel_context(self):
        self.assertQuerysetEqual(self.response.context['hotels'],
                                 [self.hotel])

    def test_template_contains_hotel_images(self):
        self.assertQuerysetEqual(self.response.context['hotel_images'], [
                                 create_hotel_image_test_object(self.hotel, 'https://myimage.com/hotelImage')])


class HomePageTourContextTest(HomePageTestSetup):
    def setUp(self):
        super().setUp()
        self.tour = create_tour_test_object(
            'Mountain View', 150, 'Best tour', 20, 15)

    def test_template_contains_correct_tour_context(self):
        self.assertQuerysetEqual(self.response.context['tours'], [self.tour])

    def test_template_contains_tour_images(self):
        self.assertQuerysetEqual(self.response.context['tour_images'],
                                 [create_tour_image_test_object(self.tour, 'https://myimage.com/tourImage')])
