from server.apps.hotels.models import Hotel


def create_test_hotel_object():
    return Hotel.objects.create(hotel_name='test_hotel', no_of_rooms=0, price_per_night=0, hotel_description='')
