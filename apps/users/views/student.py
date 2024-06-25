from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import logout
from apps.users.models import CustomUser
from apps.users.filters import StudentFilter
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from apps.users.forms import ParentRegisterForm, TeacherRegisterForm, StudentRegisterForm, AdminRegisterForm
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView


class UserRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'admit-form.html'
    model = get_user_model()


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'update-form.html'
    model = get_user_model()


class StudentRegisterView(UserRegisterView):
    form_class = StudentRegisterForm
    permission_required = ('users.add_students',)
    success_url = reverse_lazy('users:student_list')

    def form_valid(self, form):
        form.instance.role = CustomUser.Role.STUDENT.value
        return super().form_valid(form)


class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'all-student.html'
    queryset = CustomUser.objects.filter(role=CustomUser.Role.STUDENT.value)
    context_object_name = 'students'
    permission_required = ('users.view_students',)

    def get_queryset(self):
        user = self.request.user
        match user.role:
            case CustomUser.Role.PARENT.value:
                self.queryset = user.children.all()
            case CustomUser.Role.TEACHER.value:
                 self.queryset = user.get_all_student_in_group(user)
        self.filterset = StudentFilter(self.request.GET, queryset=self.queryset)
        self.queryset = self.filterset.qs
        username = self.request.GET.get('username')
        query_id = self.request.GET.get('id')
        name = self.request.GET.get('name')
        if username:
            self.queryset = self.queryset.filter(
                                                 Q(phone_number__icontains=username) | 
                                                 Q(email__icontains=username))
        if query_id:
            self.queryset = self.queryset.filter(pk__startswith=query_id)

        if name:
            self.queryset = self.queryset.filter(Q(first_name__icontains=name) |
                                                 Q(last_name__icontains=name) |
                                                 Q(father_name__icontains=name))
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context
    

class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student-detail.html'
    queryset = CustomUser.objects.filter(role=CustomUser.Role.STUDENT.value)
    context_object_name = 'student'
    permission_required = ('users.view_students',)

    def get_object(self):
        user = self.request.user
        pk = self.kwargs[self.pk_url_kwarg]
        try:
            obj = CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise ObjectDoesNotExist()

        match user.role:
            case CustomUser.Role.PARENT.value:
                if obj not in user.children.all():
                    raise PermissionDenied("You are not authorized to view this student")
            case CustomUser.Role.TEACHER.value:
                if obj not in user.get_all_student_in_group(user):
                    raise PermissionDenied("This is not your student")
        return obj


class StudentUpdateView(UserUpdateView):
    form_class = StudentRegisterForm
    permission_required = ('users.change_students',)
    success_url = reverse_lazy('users:student_list')


class SearchStudentView(LoginRequiredMixin, TemplateView):
    template_name = 'student-promotion.html'


class StudentDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index3.html'