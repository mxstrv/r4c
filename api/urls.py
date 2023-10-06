from django.urls import path

from api.views import create_robot

urlpatterns = [
    path('create-robot/', create_robot, name='create_robot')
]
