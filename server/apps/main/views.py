from django.shortcuts import render
from server.apps.hotels.models import Hotel


def index(request):
    hotels = Hotel.objects.all()
    context = {'hotels': hotels}
    return render(request, 'index.html', status=200, context=context)
