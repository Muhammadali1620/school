from django.shortcuts import render
from django.views.generic import TemplateView


class ExamScheduleTemplateView(TemplateView):
    template_name = "exam-schedule.html"


class ExamGradeTemplateView(TemplateView):
    template_name = "exam-grade.html"