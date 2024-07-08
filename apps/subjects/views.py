from django.shortcuts import redirect
from django.views.generic import ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from decimal import Decimal
from django.http import HttpResponseRedirect
from autoslug import AutoSlugField
from .forms import SubjectForm
from apps.subjects.models import Subject
from django.contrib import messages


class SubjectListView(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    template_name = 'subjects/all-subject.html'
    context_object_name = 'subjects'
    permission_required = ('subjects.view_subject',)

    def get_queryset(self):
        queryset = Subject.objects.all()

        search_id = self.request.GET.get('search_id')
        if search_id:
            queryset = queryset.filter(id__startswith=search_id)

        search_name = self.request.GET.get('search_name')
        if search_name:
            queryset = queryset.filter(name__icontains=search_name)

        return queryset

    def post(self, request):
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')

        try:
            price = Decimal(price.replace(',', '.'))
        except ValueError:
            messages.error(request, 'Invalid price format')

        form = SubjectForm({'name':name, 'desc':desc, 'price':price})

        if form.is_valid():
            form.save()
            messages.success(request, 'Subject added successfully')

        else:
            print(form.errors)
            messages.error(request, 'Error adding subject')

        return redirect('subjects:subject_page')


class SubjectDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Subject
    template_name = 'subjects/subject_delete.html'
    permission_required = ('users.delete_customuser')
    success_url = reverse_lazy('subjects:subject_page')


class SubjectEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Subject
    fields = ['name']
    template_name = 'subjects/subject_edit.html'
    permission_required = ('users.change_customuser')
    success_url = reverse_lazy('subjects:subject_page')