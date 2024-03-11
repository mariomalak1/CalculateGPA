from django.urls import path

from . import views

urlpatterns = [
    path("registeredStudent/", views.SubjectView.as_view(), name="registeredStudent"),
    path("registeredStudent/<ref>/", views.SubjectView.as_view(), name="registeredStudentWithRef"),
    path("calculateGpa/", views.calculateGpa, name="calculateGpa"),
    path("statistics/", views.getStatistics, name="getStatistics"),
]
