from django.shortcuts import render
from django.views.generic import TemplateView


class AdditionalTemplateView(TemplateView):
    template_name = 'all-book.html'


class AddAdditionalTemplateView(TemplateView):
    template_name = 'add-book.html'