from server.apps.instructors.models import Instructor
from server.apps.ratings.models import Rating
from server.apps.tourimages.models import TourImage
from server.apps.tourinstructors.models import TourInstructor
from server.apps.tourratings.models import TourRating
from server.apps.tours.models import Tour
from server.utils.context_objects import Context


class TourContext(Context[Tour]):

    def __init__(self, tour_name: str) -> None:
        self._context_obj = Tour.objects.filter(tour_name=tour_name)

    def get_tour_name(self) -> list:
        return self._context_obj[0].tour_name

    def get_tour_price(self) -> list:
        return self._context_obj[0].tour_price

    def get_tour_duration(self) -> list:
        return self._context_obj[0].tour_duration

    def get_tour_description(self) -> list:
        return self._context_obj[0].tour_description

    def get_tour_max_participants(self) -> list:
        return self._context_obj[0].max_participants

    def get_tour_rating(self) -> list:
        return [Rating.objects.filter(pk=tour.rating.pk)[0] for tour in TourRating.objects.filter(tour__in=self._context_obj)[:1]]

    def get_tour_images(self) -> list:
        return [tour_images for tour_images in TourImage.objects.filter(tour__in=self._context_obj)[:4]]

    def get_tour_instructor(self) -> list:
        return [Instructor.objects.filter(pk=tour_instructor.instructor.pk)[0] for tour_instructor in TourInstructor.objects.filter(tour__in=self._context_obj)]


def get_context(tour_name: str) -> dict:
    tour_context_obj = TourContext(tour_name)

    return {
        'tour_name': tour_context_obj.get_tour_name(),
        'tour_price': tour_context_obj.get_tour_price(),
        'tour_description': tour_context_obj.get_tour_description(),
        'max_participants': tour_context_obj.get_tour_max_participants(),
        'tour_duration': tour_context_obj.get_tour_duration(),
        'tour_rating': tour_context_obj.get_tour_rating(),
        'tour_images': tour_context_obj.get_tour_images(),
        'tour_instructor': tour_context_obj.get_tour_instructor(),
    }
