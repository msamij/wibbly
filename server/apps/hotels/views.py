from webbrowser import get
from django.shortcuts import render


def hotels(request, hotel_name):
    return render(request, 'main.html')
