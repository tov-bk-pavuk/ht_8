from django.urls import path

from . import views

urlpatterns = [
    path('', views.people_fn),
    path('id/<int:id>', views.person_id),
    path('ed/<int:id>', views.person_ed),
]
