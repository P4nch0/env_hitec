from django.db import models

# Create your models here.

import datetime
from django.utils import timezone

class Team(models.Model):
    max = models.IntegerField(default=10)
    color = models.CharField(max_length=15)
    numero = models.IntegerField(default=1)


class Student(models.Model):
    matriucla = models.CharField(max_length=15)
    team_id = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)
    birth_date = models.DateTimeField('birth date')

    def __str__(self):
        return '{} {}'.format(self.name, self.last_name)

    def team(self):
        return self.team_id

    def bday(self):
        return self.birth_date >= timezone.now() - datetime.timedelta(days=7)  # returns true if the student's bday was during the HiTec week


