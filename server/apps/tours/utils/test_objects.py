from server.apps.tours.models import Tour


def create_test_tour_object():
    return Tour.objects.create(tour_name='test_tour', tour_price=0, tour_description='', max_participants=0, tour_duration=0)
