from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from apps.groups.models import StudentGroup


class GroupListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'all-class.html'
    permission_required = ('groups.	view_studentgroup',)


    def get_queryset(self):
        queryset = StudentGroup.objects.all()
        search_id = self.request.GET.get('search_id')
        search_name = self.request.GET.get('search_name')
        teacher_name = self.request.GET.get('teacher_name')

        if search_id:
            queryset = queryset.filter(id__startswith=search_id)

        if search_name:
            queryset = queryset.filter(subject__name__icontains=search_name)

        if teacher_name:
            queryset = queryset.filter(Q(teacher__first_name__icontains=teacher_name)
                                       |
                                       Q(teacher__last_name__icontains=teacher_name))
        return queryset


class StudentGroupCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = StudentGroup
    fields = ['subject', 'teacher', 'start_time', 'end_time', 'week_days', 'create_date', ]

    template_name = 'admit-form.html'
    permission_required = ('groups.	add_studentgroup',)
    success_url = reverse_lazy('group_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New StudentGroup'
        return context


class StudentGroupDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = StudentGroup
    template_name = 'delete_page.html'
    permission_required = ('groups.	delete_studentgroup',)
    success_url = reverse_lazy('group_list-page')


class StudentGroupUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = StudentGroup
    fields = ['subject', 'teacher', 'start_time', 'end_time', 'week_days', 'create_date', ]
    template_name = 'update-form.html'
    permission_required = ('groups.	change_studentgroup',)
    success_url = reverse_lazy('group_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New StudentGroup'
        return context


class GroupDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = StudentGroup
    template_name = 'all-group-student.html'
    permission_required = ('groups.	view_studentgroup',)


def set_language(request, lang):
    current_lang = request.GET.get('current_lang', 'en')
    next_url = request.META['HTTP_REFERER']
    next_url = str(next_url).replace(current_lang, lang, 1)
    return HttpResponseRedirect(next_url)


def home(request):
    lang = request.GET.get('language')
    context = {
        'salomlar': ['hello', 'rivet'],
        'lang': lang
    }
    return render(request, template_name='index.html', context=context)