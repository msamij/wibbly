from django.urls import path
from .views import hotels

urlpatterns = [
    path('<str:hotel>', hotels, name='hotel'),
]
