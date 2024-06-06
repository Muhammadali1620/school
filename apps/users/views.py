from django.views.generic import ListView, DetailView
from apps.users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect


def error_403(request):
    return render(request, 'errors/403.html')

#<=============>Students<=============>#
class StudentListView(LoginRequiredMixin, ListView):
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.student)
    context_object_name = 'students'
    
    def render_to_response(self, context, **response_kwargs):
        super().render_to_response(context, **response_kwargs)
        if 'users.view_customuser' in self.request.user.get_all_permissions():
            return render(self.request, template_name='all-student.html', context=context)
        else:
            return redirect('error_403')
        

class StudentDetailView(LoginRequiredMixin, DetailView):
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.student)
    context_object_name = 'student'

    def render_to_response(self, context, **response_kwargs):
        super().render_to_response(context, **response_kwargs)
        if 'users.view_customuser' in self.request.user.get_all_permissions():
            return render(self.request, template_name='student-detail.html', context=context)
        else:
            return redirect('error_403')
        
        
#<=============>Teachers<=============>#
class TeacherListView(LoginRequiredMixin, ListView):
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.teacher)
    context_object_name = 'teachers'

    def render_to_response(self, context, **response_kwargs):
        user = self.request.user
        super().render_to_response(context, **response_kwargs)
        if 'users.view_customuser' in user.get_all_permissions() and user.status == CustomUser.StatusChoices.admin:
            return render(self.request, template_name='all-teacher.html', context=context)
        else:
            return redirect('error_403')
        

class TeacherDetailView(LoginRequiredMixin, DetailView):
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.teacher)
    context_object_name = 'teacher'

    def render_to_response(self, context, **response_kwargs):
        super().render_to_response(context, **response_kwargs)
        if 'users.view_customuser' in self.request.user.get_all_permissions():
            return render(self.request, template_name='teacher-detail.html', context=context)
        else:
            return redirect('error_403')
        

#<=============>Parents<=============>#
class ParentListView(LoginRequiredMixin, ListView):
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.parent)
    context_object_name = 'parents'

    def render_to_response(self, context, **response_kwargs):
        super().render_to_response(context, **response_kwargs)
        if 'users.view_customuser' in self.request.user.get_all_permissions():
            return render(self.request, template_name='all-parents.html', context=context)
        else:
            return redirect('error_403')
        

class ParentDetailView(LoginRequiredMixin, DetailView):
    queryset = CustomUser.objects.filter(status=CustomUser.StatusChoices.parent)
    context_object_name = 'parent'

    def render_to_response(self, context, **response_kwargs):
        super().render_to_response(context, **response_kwargs)
        if 'users.view_customuser' in self.request.user.get_all_permissions():
            return render(self.request, template_name='parent-detail.html', context=context)
        else:
            return redirect('error_403')