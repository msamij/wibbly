from django.shortcuts import render
from server.apps.hotels.models import Hotel


def index(request):
    return render(request, 'index.html', status=200)


def get_hotel_data():
    return len(Hotel.objects.all())
