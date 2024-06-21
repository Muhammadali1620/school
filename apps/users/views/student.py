from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from apps.users.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from apps.users.forms import ParentRegisterForm, TeacherRegisterForm, StudentRegisterForm
from django.db.models import Q


class UserRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'admit-form.html'
    model = get_user_model()


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'update-form.html'
    model = get_user_model()


class StudentRegisterView(UserRegisterView):
    model = get_user_model()
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
        query = self.request.GET.get('query')
        if query:
            self.queryset = self.queryset.filter(Q(pk__icontains=query) |
                                                 Q(phone_number__icontains=query) | 
                                                 Q(email__icontains=query) |
                                                 Q(first_name__icontains=query) |
                                                 Q(last_name__icontains=query) |
                                                 Q(father_name__icontains=query) |
                                                 Q(bio__icontains=query))
        return self.queryset


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