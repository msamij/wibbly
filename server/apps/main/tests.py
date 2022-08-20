from django.test import Client, TestCase
from server.apps.hotels.models import Hotel
from server.apps.tours.models import Tour


def create_test_hotel_object(hotel_name: str, no_of_rooms: int, price_per_night: int, hotel_description: str) -> Hotel:
    return Hotel.objects.create(hotel_name=hotel_name,
                                no_of_rooms=no_of_rooms,
                                price_per_night=price_per_night,
                                hotel_description=hotel_description)


def create_test_tour_object(tour_name: str, tour_price: int,
                            tour_description: str, max_participants: int,
                            tour_duration: int) -> Tour:
    return Tour.objects.create(tour_name=tour_name,
                               tour_price=tour_price,
                               tour_description=tour_description,
                               max_participants=max_participants,
                               tour_duration=tour_duration)


class HomePageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get('/')

    def test_home_page_returns_correct_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'index.html')

    def test_template_contains_correct_context(self):
        self.assertQuerysetEqual(
            self.response.context['hotels'], [create_test_hotel_object('Transalvania', 100, 200, 'Best monster hotel')])
        self.assertQuerysetEqual(self.response.context['tours'],
                                 [create_test_tour_object('Mountain View', 150, 'Best tour', 20, 15)])
