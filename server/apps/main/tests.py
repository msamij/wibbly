from server.apps.activities.models import Activity
from server.apps.activityimages.models import ActivityImage
from server.apps.hotelimages.models import HotelImage
from server.apps.hotels.models import Hotel
from server.apps.tourimages.models import TourImage
from server.apps.tours.models import Tour

# These test objects will be created to test that the actual database returns them and will be injected into template.


def create_hotel_test_object(hotel_name: str, no_of_rooms: int, price_per_night:
                             int, hotel_description: str) -> Hotel:
    return Hotel.objects.create(hotel_name=hotel_name,
                                no_of_rooms=no_of_rooms,
                                price_per_night=price_per_night,
                                hotel_description=hotel_description)


def create_tour_test_object(tour_name: str, tour_price: int,
                            tour_description: str, max_participants: int,
                            tour_duration: int) -> Tour:
    return Tour.objects.create(tour_name=tour_name,
                               tour_price=tour_price,
                               tour_description=tour_description,
                               max_participants=max_participants,
                               tour_duration=tour_duration)


def create_activity_test_object(activity_name: str, activity_price: int, activity_description: str) -> Activity:
    return Activity.objects.create(activity_name=activity_name,
                                   activity_price=activity_price,
                                   activity_description=activity_description)


def create_hotel_image_test_object(hotel: Hotel, hotel_image_url: str) -> HotelImage:
    return HotelImage.objects.create(hotel=hotel, hotel_image_url=hotel_image_url)


def create_tour_image_test_object(tour: Tour, tour_image_url: str) -> TourImage:
    return TourImage.objects.create(tour=tour, tour_image_url=tour_image_url)


def create_activity_image_test_object(activity: Activity, activity_image_url: str) -> ActivityImage:
    return ActivityImage.objects.create(activity=activity, activity_image_url=activity_image_url)


# class HomePageTemplateContextTest(HomePageTest):
#     def setUp(self):
#         super().setUp()
#         self.hotel = create_hotel_test_object(
#             'Transalvania', 100, 200, 'Best monster hotel')
#         self.tour = create_tour_test_object(
#             'Mountain View', 150, 'Best tour', 20, 15)
#         self.activity = create_activity_test_object(
#             'Cycling', 100, 'Best activity')

#     def test_template_contains_correct_hotel_context(self):
#         self.assertQuerysetEqual(self.response.context['hotels'],
#                                  [self.hotel])

#     def test_template_contains_correct_tour_context(self):
#         self.assertQuerysetEqual(self.response.context['tours'], [self.tour])

#     def test_template_contains_correct_activity_context(self):
#         self.assertQuerysetEqual(
#             self.response.context['activities'], [self.activity])

#     def test_template_contains_activity_images(self):
#         self.assertQuerysetEqual(self.response.context['activity_images'],
#                                  [create_activity_image_test_object(self.activity, 'https://myimage.com/activityImage')])

#     def test_template_contains_hotel_images(self):
#         self.assertQuerysetEqual(self.response.context['hotel_images'], [
#                                  create_hotel_image_test_object(self.hotel, 'https://myimage.com/hotelImage')])

#     def test_template_contains_tour_images(self):
#         self.assertQuerysetEqual(self.response.context['tour_images'],
#                                  [create_tour_image_test_object(self.tour, 'https://myimage.com/tourImage')])
