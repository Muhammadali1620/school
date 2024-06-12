from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from apps.users.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy


#<=============>Students<=============>#
class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'all-student.html'
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.student)
    context_object_name = 'students'
    permission_required = ('users.view_customuser')


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'student-detail.html'
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.student)
    context_object_name = 'student'
    permission_required = ('users.view_customuser')


class StudentRegisterView(LoginRequiredMixin, TemplateView):
    template_name = 'admit-form.html'
        

class SearchStudentView(LoginRequiredMixin, TemplateView):
    template_name = 'student-promotion.html'


class StudentDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index3.html'
        

#<=============>Teachers<=============>#
class TeacherListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'all-teacher.html'
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.teacher)
    context_object_name = 'teachers'
    permission_required = ('users.view_customuser')
        

class TeacherDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'teacher-detail.html'
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.teacher)
    context_object_name = 'teacher'
    permission_required = ('users.view_customuser')


class TeacherRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = get_user_model()
    fields = ['first_name', 'last_name','father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number', 'password',
               'subject', 'address', 'gender', 'salary', 'image', 'bio', 'zip_code']
    template_name = 'add-teacher.html'
    permission_required = ('users.add_customuser')
    success_url = reverse_lazy('users:teacher_list')

    def form_valid(self, form):
        form.instance.status = CustomUser.StatusChoices.teacher
        return super().form_valid(form)


class TeacherDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index5.html'


#<=============>Parents<=============>#
class ParentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'all-parent.html'
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.parent)
    context_object_name = 'parents'
    permission_required = ('users.view_customuser')


class ParentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'parent-detail.html'
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.parent)
    context_object_name = 'parent'
    permission_required = ('users.view_customuser')


class AddParentView(LoginRequiredMixin, TemplateView):
    template_name = 'add-parent.html'


class ParentDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index4.html'


#<=============>Account Settings<=============>#
class AccountSettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'account-settings.html'


class UserLoginView(LoginView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)
    

class UserLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


#<=============>Errors<=============>#
def error_403(request):
    return render(request, 'errors/403.html')