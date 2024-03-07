from django.db import models
from Authentication.models import Student

from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User as DjangoUser

# Create your models here.

class Subject(models.Model):
    gradeChosies = ((4, "A+"), (3.7, "A"), (3.3, "B+"), (3, "B"), (2.7, "C+"), (2.4, "C"), (2, "D+"), (2, "D"),)
    TermNumber = ((1, "First Term"), (2, "Second Term"),)
    YearNumber = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7))
    subject_name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    grade = models.FloatField(null=False, blank=False, choices=gradeChosies)
    term = models.PositiveSmallIntegerField(null=False, blank=False, choices=TermNumber)
    year = models.PositiveSmallIntegerField(null=False, blank=False, choices=YearNumber)
    creadit_Hours = models.PositiveSmallIntegerField(null=False, blank=False)
    ref = models.SlugField(null=False, blank=False, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def calculateNumberOfPoints(self):
        return self.grade * self.creadit_Hours

    def __str__(self):
        return self.ref

    def save(self, *args, **kwargs):
        self.ref = slugify(self.subject_name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["year", "term"]
