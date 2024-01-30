from django.db import models
from django.contrib.auth.models import User as djangoUser
# Create your models here.

class Subject(models.Model):
    gradeChosies = (("A+", 4), ("A", 3.7), ("B+", 3.3), ("B", 3), ("C+", 2.7), ("C", 2.4), ("D+", 2), ("D", 2),)
    subName = models.CharField(max_length=120, null=False)
    grade = models.PositiveSmallIntegerField(null=False, choices=gradeChosies)
    student = models.ForeignKey(djangoUser, on_delete=models.CASCADE)
