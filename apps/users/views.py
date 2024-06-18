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


#<=============>Students<=============>#
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
        

class StudentRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = get_user_model()
    fields = ['first_name', 'last_name','father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number', 'password',
               'student_group', 'address', 'gender', 'image', 'bio', 'zip_code']
    template_name = 'admit-form.html'
    permission_required = ('users.add_students',)
    success_url = reverse_lazy('users:student_list')

    def form_valid(self, form):
        form.instance.role = CustomUser.Role.STUDENT.value
        return super().form_valid(form)
    

class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ['first_name', 'last_name','father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number', 'password',
               'student_group', 'address', 'gender', 'image', 'bio', 'zip_code']
    template_name = 'update-form.html'
    permission_required = ('users.change_students',)
    success_url = reverse_lazy('users:student_list')


class SearchStudentView(LoginRequiredMixin, TemplateView):
    template_name = 'student-promotion.html'


class StudentDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index3.html'
        

#<=============>Teachers<=============>#
class TeacherListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'all-teacher.html'
    queryset = CustomUser.objects.filter(role=CustomUser.Role.TEACHER.value)
    context_object_name = 'teachers'
    permission_required = ('users.view_teachers',)


class TeacherUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    fields = ['first_name', 'last_name','father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number', 'password',
               'subject', 'address', 'gender', 'salary', 'image', 'bio', 'zip_code']
    template_name = 'update-form.html'
    permission_required = ('users.change_teachers',)
    success_url = reverse_lazy('users:teacher_list')
        

class TeacherDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'teacher-detail.html'
    queryset = CustomUser.objects.filter(role=CustomUser.Role.TEACHER.value)
    context_object_name = 'teacher'
    permission_required = ('users.view_teachers',)


class TeacherRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = get_user_model()
    fields = ['first_name', 'last_name','father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number', 'password',
               'subject', 'address', 'gender', 'salary', 'image', 'bio', 'zip_code']
    template_name = 'admit-form.html'
    permission_required = ('users.add_teachers',)
    success_url = reverse_lazy('users:teacher_list')

    def form_valid(self, form):
        form.instance.role = CustomUser.Role.TEACHER.value
        return super().form_valid(form)


class TeacherDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index5.html'


#<=============>Parents<=============>#
class ParentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'all-parent.html'
    queryset = CustomUser.objects.filter(role=CustomUser.Role.PARENT.value)
    context_object_name = 'parents'
    permission_required = ('users.view_parents',)


class ParentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'parent-detail.html'
    queryset = CustomUser.objects.filter(role=CustomUser.Role.PARENT.value)
    context_object_name = 'parent'
    permission_required = ('users.view_parents',)


class ParentRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = get_user_model()
    fields = ['first_name', 'last_name','father_name', 'date_of_birth', 'email', 'phone_number', 'password',
               'children', 'address', 'gender', 'image', 'bio', 'zip_code']
    template_name = 'admit-form.html'
    permission_required = ('users.add_parents',)
    success_url = reverse_lazy('users:parent_list')

    def form_valid(self, form):
        form.instance.role = CustomUser.Role.PARENT.value
        return super().form_valid(form)
    

class ParentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'update-form.html'
    fields = ['first_name', 'last_name','father_name', 'date_of_birth', 'email', 'phone_number', 'password',
               'children', 'address', 'gender', 'image', 'bio', 'zip_code']
    permission_required = ('users.change_parents',)
    success_url = reverse_lazy('users:parent_list')



class ParentDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index4.html'


#<=============>Account Settings<=============>#
class AccountSettings(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = get_user_model()
    fields = ['first_name', 'last_name','father_name', 'date_of_birth', 'email', 'phone_number', 'password',
              'address', 'gender', 'image', 'bio', 'zip_code']
    template_name = 'admit-form.html'
    permission_required = ('users.add_admins',)
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.role = CustomUser.Role.ADMIN.value
        return super().form_valid(form)


class UserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = 'delete_page.html'
    permission_required = ('users.change_customuser',)

    def form_valid(self, form):
        if self.get_object().role == CustomUser.Role.TEACHER.value and self.get_object().teacher_groups:
            messages.error(self.request, 'You cannot delete a teacher while he has groups!')
            return redirect(self.request.META['HTTP_REFERER'])
        else:
            return super().form_valid(form)

    def get_success_url(self):
        if self.get_object().role == CustomUser.Role.STUDENT.value:
            return reverse_lazy('users:student_list')
        if self.get_object().role == CustomUser.Role.TEACHER.value:
            return reverse_lazy('users:teacher_list')
        if self.get_object().role == CustomUser.Role.PARENT.value:
            return reverse_lazy('users:parent_list')


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