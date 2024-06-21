from .student import *


class TeacherRegisterView(UserRegisterView):
    form_class = TeacherRegisterForm
    permission_required = ('users.add_teachers',)
    success_url = reverse_lazy('users:teacher_list')

    def form_valid(self, form):
        form.instance.role = CustomUser.Role.TEACHER.value
        return super().form_valid(form)


class TeacherListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'all-teacher.html'
    queryset = CustomUser.objects.filter(role=CustomUser.Role.TEACHER.value)
    context_object_name = 'teachers'
    permission_required = ('users.view_teachers',)


class TeacherUpdateView(UserUpdateView):
    form_class = TeacherRegisterForm
    permission_required = ('users.change_teachers',)
    success_url = reverse_lazy('users:teacher_list')
        

class TeacherDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'teacher-detail.html'
    queryset = CustomUser.objects.filter(role=CustomUser.Role.TEACHER.value)
    context_object_name = 'teacher'
    permission_required = ('users.view_teachers',)


class TeacherDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index5.html'