from server.apps.activities.models import Activity
from server.apps.activityimages.models import ActivityImage
from server.apps.hotelimages.models import HotelImage
from server.apps.hotels.models import Hotel
from server.apps.tourimages.models import TourImage
from server.apps.tours.models import Tour

# These objects will be created during tests to test that the template context contains these objects.


def create_hotel_image_test_object(hotel: Hotel) -> HotelImage:
    return HotelImage.objects.create(hotel=hotel, hotel_image_url='test_hotel_image_url')


def create_tour_image_test_object(tour: Tour) -> TourImage:
    return TourImage.objects.create(tour=tour, tour_image_url='test_tour_image_url')


def create_activity_image_test_object(activity: Activity) -> ActivityImage:
    return ActivityImage.objects.create(activity=activity, activity_image_url='test_activity_image_url')


def create_hotel_test_object() -> Hotel:
    return Hotel.objects.create(hotel_name='test_hotel_name', no_of_rooms=0,
                                price_per_night=0, hotel_description='test_hotel_description')


def create_tour_test_object() -> Tour:
    return Tour.objects.create(tour_name='test_tour_name', tour_price=0,
                               tour_description='test_tour_description', max_participants=0,
                               tour_duration=0)


def create_activity_test_object() -> Activity:
    return Activity.objects.create(activity_name='test_activity_name', activity_price=0,
                                   activity_description='test_activity_description')
