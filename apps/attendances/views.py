from django.shortcuts import render
from django.views.generic import TemplateView


class StudentAttendanceTemplateView(TemplateView):
    template_name = "student-attendance.html"