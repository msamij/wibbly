from django.shortcuts import render
from server.apps.main.utils.context_objects import *


def index(request):
    context = {
        'activities': get_activity_with_images(),
        'hotels': get_hotel_with_images(),
        'tours': get_tour_with_images(),
    }
    return render(request, 'index.html', status=200, context=context)
