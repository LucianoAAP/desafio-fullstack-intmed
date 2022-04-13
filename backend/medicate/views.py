from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from medicate.models import Doctors, Appointments, Schedules
from medicate.serializers import (
    DoctorsSerializer, Appointments, SchedulesSerializer)


@csrf_exempt
def doctors_api(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                doctor = Doctors.objects.get(id=id)
                doctors_serializer = DoctorsSerializer(doctor)
                return JsonResponse(doctors_serializer.data, safe=False)
            except Doctors.DoesNotExist:
                return JsonResponse('Not found', safe=False, status=404)
        doctors = Doctors.objects.all()
        doctors_serializer = DoctorsSerializer(doctors, many=True)
        return JsonResponse(doctors_serializer.data, safe=False)

    elif request.method == 'POST':
        doctors_data = JSONParser().parse(request)
        doctors_serializer = DoctorsSerializer(data=doctors_data)
        if doctors_serializer.is_valid():
            doctors_serializer.save()
            return JsonResponse('Added successfully', safe=False, status=201)
        return JsonResponse('Failed to add', safe=False, status=400)

    elif request.method == 'PUT':
        try:
            doctors_data = JSONParser().parse(request)
            doctor = Doctors.objects.get(id=id)
            doctors_serializer = DoctorsSerializer(doctor, data=doctors_data)
            if doctors_serializer.is_valid():
                doctors_serializer.save()
                return JsonResponse('Updated successfully', safe=False)
            return JsonResponse('Failed to update', safe=False, status=400)
        except Doctors.DoesNotExist:
            return JsonResponse('Not found', safe=False, status=404)

    elif request.method == 'DELETE':
        try:
            doctor = Doctors.objects.get(id=id)
            doctor.delete()
            return JsonResponse('', safe=False)
        except Doctors.DoesNotExist:
            return JsonResponse('Not found', safe=False, status=404)
