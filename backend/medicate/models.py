from django.db import models


class Doctors(models.Model):
    name = models.CharField(max_length=250)
    crm = models.PositiveIntegerField(default=1)
    email = models.CharField(max_length=100, blank=True)


class Appointments(models.Model):
    day = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)


class Schedules(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    day = models.DateField()
    schedules = models.ForeignKey(Appointments, on_delete=models.CASCADE)
