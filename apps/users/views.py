from django.views.generic import ListView
from apps.users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect


def error_403(request):
    return render(request, 'errors/403.html')


class StudentListView(LoginRequiredMixin, ListView):
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.student)
    context_object_name = 'students'
    
    def render_to_response(self, context, **response_kwargs):
        super().render_to_response(context, **response_kwargs)
        if 'users.view_customuser' in self.request.user.get_all_permissions():
            return render(self.request, template_name='all-student.html', context=context)
        else:
            return redirect('error_403')