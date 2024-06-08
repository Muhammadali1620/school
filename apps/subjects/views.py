from django.shortcuts import render
from django.views.generic import TemplateView


class SubjectTemplateView(TemplateView):
    template_name = 'all-subject.html'