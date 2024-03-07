from django.urls import path

from . import views

urlpatterns = [
    path("getAllRegisteredStudent/", views.registerSubjects, name="getAllRegisteredStudent"),
]
