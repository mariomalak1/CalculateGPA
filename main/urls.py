from django.urls import path

from . import views

urlpatterns = [
    path("registeredStudent/", views.registerSubjects, name="registeredStudent"),
    path("calculateGpa/", views.calculateGpa, name="calculateGpa"),
    path("statistics/", views.getStatistics, name="getStatistics"),
]
