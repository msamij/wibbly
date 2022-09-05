from server.apps.activities.models import Activity
from server.apps.activityimages.models import ActivityImage
from server.apps.activityinstructors.models import ActivityInstructor
from server.apps.activityratings.models import ActivityRating
from server.apps.instructors.models import Instructor
from server.apps.ratings.models import Rating
from server.utils.context_objects import Context


class ActivityContext(Context[Activity]):

    def __init__(self, activity_name: str) -> None:
        super().__init__(Activity, activity_name)

    def get_activity_name(self) -> list:
        return self.get_context_obj_name()

    def get_activity_price(self) -> list:
        return self.get_context_obj_price()

    def get_activity_description(self) -> list:
        return self.get_context_obj_description()

    def get_activity_rating(self) -> list:
        return [Rating.objects.filter(pk=activity.rating.pk)[0] for activity in ActivityRating.objects.filter(activity__in=self._context_obj)[:1]]

    def get_activity_images(self) -> list:
        return [activity_images for activity_images in ActivityImage.objects.filter(activity__in=self._context_obj)[:4]]

    def get_activity_instructor(self) -> list:
        return [Instructor.objects.filter(pk=activity_instructor.instructor.pk)[0] for activity_instructor in ActivityInstructor.objects.filter(activity__in=self._context_obj)]


def get_context(activity_name: str) -> dict:
    activity_context_obj = ActivityContext(activity_name)

    return {
        'activity_name': activity_context_obj.get_activity_name(),
        'activity_price': activity_context_obj.get_activity_price(),
        'activity_description': activity_context_obj.get_activity_description(),
        'activity_rating': activity_context_obj.get_activity_rating(),
        'activity_images': activity_context_obj.get_activity_images(),
        'activity_instructor': activity_context_obj.get_activity_instructor(),
    }
