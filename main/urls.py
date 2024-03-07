from django.urls import path

from . import views

urlpatterns = [
    path("registeredStudent/", views.registerSubjects, name="getAllRegisteredStudent"),
    path("calculateGpa/", views.calculateGpa, name="calculateGpa"),
]
