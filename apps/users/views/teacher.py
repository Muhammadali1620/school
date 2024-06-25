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

    def get_queryset(self):
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