from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from apps.additionals.models import AdditionalTask
from django.urls import reverse_lazy
from .forms import AdditionalTaskForm



class AdditionalListView(ListView):
    template_name = 'all-book.html'
    queryset = AdditionalTask.objects.all().select_related('subject').order_by('subject__name')
    context_object_name = 'tasks'


class AddAdditionalCreateView(CreateView):
    model = AdditionalTask
    template_name = 'add-book.html'
    form_class = AdditionalTaskForm
    success_url = reverse_lazy('adittionals:all_additional')


class AdditionalUpdateView(UpdateView):
    model = AdditionalTask
    template_name = 'add-book.html'
    form_class = AdditionalTaskForm
    success_url = reverse_lazy('adittionals:all_additional')


class AdditionalDeleteView(DeleteView):
    model = AdditionalTask
    template_name = 'delete-book.html'
    success_url = reverse_lazy('adittionals:all_additional')