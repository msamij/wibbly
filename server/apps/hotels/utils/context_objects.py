from server.apps.hotelimages.models import HotelImage
from server.apps.hotels.models import Hotel, HotelAddress


class HotelContext():
    __hotel: Hotel

    def __init__(self, hotel_name: str) -> None:
        self.__hotel = Hotel.objects.filter(hotel_name=hotel_name)

    def get_hotel_name(self) -> list:
        return self.__hotel[0].hotel_name

    def get_total_hotel_rooms(self) -> list:
        return self.__hotel[0].no_of_rooms

    def get_hotel_price(self) -> list:
        return self.__hotel[0].price_per_night

    def get_hotel_description(self) -> list:
        return self.__hotel[0].hotel_description

    def get_hotel_address(self) -> list:
        return [hotel_address for hotel_address in HotelAddress.objects.filter(hotel__in=self.__hotel)]

    def get_hotel_images(self) -> list:
        return [hotel_images for hotel_images in HotelImage.objects.filter(hotel__in=self.__hotel)[:4]]


def get_context(hotel_name: str) -> dict:
    hotel_context_obj = HotelContext(hotel_name)

    return {
        'hotel_name': hotel_context_obj.get_hotel_name(),
        'no_of_rooms': hotel_context_obj.get_total_hotel_rooms(),
        'price_per_night': hotel_context_obj.get_hotel_price(),
        'hotel_description': hotel_context_obj.get_hotel_description(),
        'hotel_address': hotel_context_obj.get_hotel_address(),
        'hotel_images': hotel_context_obj.get_hotel_images(),
    }
