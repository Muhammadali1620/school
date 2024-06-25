from .student import *


class AccountSettings(UserRegisterView):
    permission_required = ('users.add_admins',)
    form_class = AdminRegisterForm
    success_url = reverse_lazy('home')
    permission_required = 'users.add_admin'

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