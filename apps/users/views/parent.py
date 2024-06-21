from .student import *


class ParentRegisterView(UserRegisterView):
    form_class = ParentRegisterForm
    permission_required = ('users.add_parents',)
    success_url = reverse_lazy('users:parent_list')

    def form_valid(self, form):
        form.instance.role = CustomUser.Role.PARENT.value
        return super().form_valid(form)


class ParentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'all-parent.html'
    queryset = CustomUser.objects.filter(role=CustomUser.Role.PARENT.value)
    context_object_name = 'parents'
    permission_required = ('users.view_parents',)

    def get_queryset(self):
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


class ParentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'parent-detail.html'
    queryset = CustomUser.objects.filter(role=CustomUser.Role.PARENT.value)
    context_object_name = 'parent'
    permission_required = ('users.view_parents',)
    

class ParentUpdateView(UserUpdateView):
    form_class = ParentRegisterForm
    permission_required = ('users.change_parents',)
    success_url = reverse_lazy('users:parent_list')



class ParentDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index4.html'
