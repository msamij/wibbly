from django.shortcuts import render
from server.apps.activities.models import Activity
from server.apps.activityimages.models import ActivityImage
from server.apps.hotelimages.models import HotelImage
from server.apps.hotels.models import Hotel
from server.apps.tourimages.models import TourImage
from server.apps.tours.models import Tour


def index(request):
    context = {
        'hotels': Hotel.objects.all()[:4],
        'tours': Tour.objects.all()[:4],
        'activities': Activity.objects.all()[:4],
        'hotel_images': HotelImage.objects.all()[:4],
        'tour_images': TourImage.objects.all()[:4],
        'activity_images': ActivityImage.objects.all()[:4],
    }
    return render(request, 'index.html', status=200, context=context)
