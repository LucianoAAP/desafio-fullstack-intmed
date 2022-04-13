from rest_framework import serializers
from medicate.models import Doctors, Appointments, Schedules


class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ('id', 'name', 'crm', 'email')


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ('id', 'day', 'time', 'doctor')


class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ('id', 'doctor', 'day', 'schedules')
