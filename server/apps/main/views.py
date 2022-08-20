from django.shortcuts import render
from server.apps.hotels.models import Hotel
from server.apps.tours.models import Tour


def index(request):
    hotels = Hotel.objects.all()[:4]
    tours = Tour.objects.all()[:4]
    context = {
        'hotels': hotels,
        'tours': tours,

    }
    return render(request, 'index.html', status=200, context=context)
