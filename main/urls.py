from django.urls import path

from . import views

urlpatterns = [
    path("getAllRegisteredStudent/", views.getAllRegisterSubjects, name="getAllRegisteredStudent"),
]
