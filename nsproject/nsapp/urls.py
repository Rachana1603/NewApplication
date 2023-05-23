from django.contrib import admin
from django.urls import path
from .views import InstructorView,CourseView

urlpatterns = [
    
    path('instructor',InstructorView.as_view()),
    path('course',CourseView.as_view())
]