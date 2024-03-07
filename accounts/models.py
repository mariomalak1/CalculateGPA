from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    Gpa = models.FloatField(null=True, blank=True)

    def calculate_Gpa(self):
        subjects = main.models.Subject.objects.filter(student_id=self.id).all()
        points = 0
        hours = 0
        for subject in subjects:
            points += subject.calculateNumberOfPoints()
            hours += subject.creadit_Hours

        self.Gpa = points / hours
        self.save()

    def __str__(self):
        return str(self.id)

import main.models
