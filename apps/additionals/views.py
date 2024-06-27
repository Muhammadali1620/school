from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from apps.additionals.models import AdditionalTask



class AdditionalListView(ListView):
    template_name = 'all-book.html'
    queryset = AdditionalTask.objects.all().select_related('subject').order_by('subject__name')
    context_object_name = 'tasks'


class AddAdditionalTemplateView(TemplateView):
    template_name = 'add-book.html'