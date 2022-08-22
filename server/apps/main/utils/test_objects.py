from server.apps.activities.models import Activity
from server.apps.activityimages.models import ActivityImage
from server.apps.hotelimages.models import HotelImage
from server.apps.hotels.models import Hotel
from server.apps.tourimages.models import TourImage
from server.apps.tours.models import Tour

# These test objects will be created during tests to test that template context contains these objects.


def create_hotel_image_test_object(hotel: Hotel, hotel_image_url: str) -> HotelImage:
    return HotelImage.objects.create(hotel=hotel, hotel_image_url=hotel_image_url)


def create_tour_image_test_object(tour: Tour, tour_image_url: str) -> TourImage:
    return TourImage.objects.create(tour=tour, tour_image_url=tour_image_url)


def create_activity_image_test_object(activity: Activity, activity_image_url: str) -> ActivityImage:
    return ActivityImage.objects.create(activity=activity, activity_image_url=activity_image_url)


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
