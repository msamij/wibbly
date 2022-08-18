from django.urls import path
from .views import hotels

urlpatterns = [
    path('<str:hotel_name>/', hotels, name='hotels'),
]
