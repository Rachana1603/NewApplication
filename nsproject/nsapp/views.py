from django.shortcuts import render
from rest_framework import generics
from .models import Instructor,Course
from .serializers import InstructorSerializer,CourseSerializer

# Create your views here.

class InstructorView(generics.ListCreateAPIView):
    queryset=Instructor.objects.all()
    serializer_class=InstructorSerializer


class CourseView(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

