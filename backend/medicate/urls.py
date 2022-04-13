from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^doctors$', views.doctors_api),
    re_path(r'^doctors/([0-9]+)$', views.doctors_api)
]
