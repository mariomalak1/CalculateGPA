from django.db import models
from Authentication.models import Student
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
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def calculateNumberOfPoints(self):
        return self.grade * self.creadit_Hours

    def __str__(self):
        grade = ""
        term = ""
        for i in self.gradeChosies:
            if self.grade == i[0]:
                grade = i[1]

        for i in self.TermNumber:
            if self.term == i[0]:
                term = i[1]

        return "Student ID : " + self.student.username + " - Subject Name : " + self.subject_name + " : Creadit Hours : " + str(self.creadit_Hours )+ " - Grade : " + grade + " : year: " + str(self.year) + " : " + term

