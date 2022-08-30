from server.apps.ratings.models import Rating
from server.apps.tourimages.models import TourImage
from server.apps.tourratings.models import TourRating
from server.apps.tourinstructors.models import TourInstructor
from server.apps.instructors.models import Instructor
from server.apps.tours.models import Tour


def get_context(tour_name: str) -> dict:
    # tour = get_tour(tour_name)
    # tour_rating = get_tour_rating(tour)
    # tour_images = get_tour_images(tour)
    # tour_instructor = get_tour_instructor(tour)
    tour_name = get_tour_name(tour_name)
    tour_price = get_tour_price(tour_name)
    tour_description = get_tour_description(tour_name)
    max_participants = get_tour_max_participants(tour_name)
    tour_duration = get_tour_duration(tour_name)

    return {
        'tour_name': tour_name,
        'tour_price': tour_price,
        'tour_description': tour_description,
        'max_participants': max_participants,
        'tour_duration': tour_duration,
        # 'tour_rating': tour_rating,
        # 'tour_images': tour_images,
        # 'tour_instructor': tour_instructor,
    }


# def get_tour(tour_name: str) -> list:
#     return [tour for tour in Tour.objects.filter(tour_name=tour_name)]


def get_tour_name(tour_name: str) -> list:
    return Tour.objects.filter(tour_name=tour_name)[0].tour_name


def get_tour_price(tour_name: str) -> list:
    return Tour.objects.filter(tour_name=tour_name)[0].tour_price


def get_tour_duration(tour_name: str) -> list:
    return Tour.objects.filter(tour_name=tour_name)[0].tour_duration


def get_tour_description(tour_name: str) -> list:
    return Tour.objects.filter(tour_name=tour_name)[0].tour_description


def get_tour_max_participants(tour_name: str) -> list:
    return Tour.objects.filter(tour_name=tour_name)[0].max_participants

# def get_tour_rating(tour: Tour) -> list:
#     return [Rating.objects.filter(pk=tour.rating.pk)[0] for tour in TourRating.objects.filter(tour__in=tour)[:1]]


# def get_tour_images(tour: Tour) -> list:
#     return [tour_image for tour_image in TourImage.objects.filter(tour__in=tour)[:4]]


# def get_tour_instructor(tour: Tour) -> list:
#     return [Instructor.objects.filter(pk=tour_instructor.instructor.pk)[0] for tour_instructor in TourInstructor.objects.filter(tour__in=tour)]
