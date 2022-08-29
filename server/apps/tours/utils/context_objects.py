from server.apps.ratings.models import Rating
from server.apps.tourimages.models import TourImage
from server.apps.tourratings.models import TourRating
from server.apps.tourinstructors.models import TourInstructor
from server.apps.instructors.models import Instructor
from server.apps.tours.models import Tour


def get_context(tour_name: str) -> dict:
    tour = get_tour(tour_name)
    tour_rating = get_tour_rating(tour)
    tour_images = get_tour_images(tour)
    tour_instructor = get_tour_instructor(tour)

    return {
        'tour': tour,
        'tour_rating': tour_rating,
        'tour_images': tour_images,
        'tour_instructor': tour_instructor,
    }


def get_tour(tour_name: str) -> list:
    return [tour for tour in Tour.objects.filter(tour_name=tour_name)]


def get_tour_rating(tour: Tour) -> list:
    return [Rating.objects.filter(pk=tour.rating.pk)[0] for tour in TourRating.objects.filter(tour__in=tour)[:1]]


def get_tour_images(tour: Tour) -> list:
    return [tour_image for tour_image in TourImage.objects.filter(tour__in=tour)[:4]]


def get_tour_instructor(tour: Tour) -> list:
    return [Instructor.objects.filter(pk=tour_instructor.instructor.pk)[0] for tour_instructor in TourInstructor.objects.filter(tour__in=tour)]
