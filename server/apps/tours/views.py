from django.shortcuts import render
from .utils.context_objects import *


def tour(request, tour: str):
    context = {
        'tour': get_tour(tour),
        'tour_rating': get_tour_rating(tour),
    }
    return render(request, 'main.html', status=200, context=context)
