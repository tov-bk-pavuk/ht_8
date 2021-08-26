from django.urls import path

from . import views

urlpatterns = [
    path('', views.people_fn),
    path('<int:p_id>', views.person_id),
]
