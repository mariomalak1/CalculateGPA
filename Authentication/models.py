from datetime import datetime, timedelta
import random
import string
import pytz

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Student(AbstractUser):
    email = models.EmailField(blank=False, null=False)
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


class ResetCode(models.Model):
    resetUser = models.ForeignKey(Student, on_delete=models.CASCADE)
    generatedCode = models.CharField(max_length=15)
    sendTime = models.DateTimeField()
    confirmedTime = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if the object is newly created
            generated_code = ResetCode.generateUniqueCode()
            while generated_code:
                if ResetCode.objects.filter(generatedCode=generated_code).first():
                    generated_code = ResetCode.generateUniqueCode()
                else:
                    break
            self.generatedCode = generated_code
            self.sendTime = datetime.now()
        super(ResetCode, self).save(*args, **kwargs)

    @staticmethod
    def generateUniqueCode():
        code = ''
        for i in range(6):
            code += random.choice(string.digits)
        return code


    # to check that is passed 15 min from time of send code
    def isCodeExpired(self):
        timeNow = datetime.now()
        quaterHour = timedelta(minutes=15)
        timeAfterQuarter = self.sendTime + quaterHour

        # to make timeNow aware datetime
        timeNow = timeNow.replace(tzinfo=pytz.utc)

        if timeNow >= timeAfterQuarter:
            return True
        return False

        # if self.confirmedTime:
        #     if timeNow >= self.confirmedTime + quaterHour:
        #         return True

    def __str__(self):
        return self.generatedCode
