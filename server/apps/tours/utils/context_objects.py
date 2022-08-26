from server.apps.tours.models import Tour
from server.apps.tourratings.models import TourRating
from server.apps.ratings.models import Rating


def get_tour(tour_name: str) -> list:
    return Tour.objects.filter(tour_name=tour_name)


def get_tour_rating(tour: str) -> list:
    tour_obj = Tour.objects.filter(tour_name=tour)
    return [Rating.objects.filter(rating=tour.rating)[0] for tour in TourRating.objects.filter(tour=tour_obj)[:1]]
