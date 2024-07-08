from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from apps.groups.models import StudentGroup


class GroupListView(ListView):
    template_name = 'all-class.html'

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
            queryset = queryset.filter(Q(teacher__last_name__endswith=teacher_name)
                                       |
                                       Q(teacher__last_name__endswith=teacher_name))
        return queryset


class StudentGroupCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = StudentGroup
    fields = ['subject', 'teacher', 'start_time', 'end_time', 'week_days', 'create_date', ]

    template_name = 'admit-form.html'
    permission_required = ('student_group.add_student_group',)
    success_url = reverse_lazy('group_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New StudentGroup'
        return context


class StudentGroupDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = StudentGroup
    template_name = 'users_delete.html'
    permission_required = ('student_group.delete_student_group',)
    success_url = reverse_lazy('group_list-page')


class StudentGroupUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = StudentGroup
    fields = ['subject', 'teacher', 'start_time', 'end_time', 'week_days', 'create_date', ]
    template_name = 'users_update.html'
    permission_required = ('student_group.change_payment',)
    success_url = reverse_lazy('group_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New StudentGroup'
        return context


class GroupDetailView(DetailView):
    model = StudentGroup
    template_name = 'all-group-student.html'
