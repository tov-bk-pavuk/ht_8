from django.urls import path

from . import views

urlpatterns = [
    path('', views.people, name='people/templates/people'),
]
