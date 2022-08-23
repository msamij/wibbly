from server.apps.hotelimages.models import HotelImage
from server.apps.hotels.models import Hotel


def get_hotel_images(hotel: Hotel) -> list:
    hotel_images = []
    for h in hotel.objects.all():
        hotel_images.append(HotelImage.objects.get(hotel=h.pk)[0])
    return hotel_images
