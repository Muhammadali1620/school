from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.exams.forms import ExamForm, ExamResultForm
from apps.exams.models import Exam, ExamResult
from apps.subjects.models import Subject
from django.contrib.auth import get_user_model
from apps.users.models import CustomUser
from django.contrib import messages


# class ExamScheduleTemplateView(TemplateView):
#     template_name = "exam-schedule.html"


# class ExamGradeTemplateView(TemplateView):
#     template_name = "exam-grade.html"


class ExamScheduleListView(ListView):
    template_name = 'exams/exam-schedule.html'
    context_object_name = 'exams'

    def get_queryset(self):
        queryset = Exam.objects.all().select_related('subject')
        search_title = self.request.GET.get('search_title')
        if search_title:
            queryset = queryset.filter(title_uz__icontains=search_title)

        subject = self.request.GET.get('subject')
        if subject:
            queryset = queryset.filter(subject__name_uz__icontains='История')
        
        print(queryset)
        return queryset

    def post(self, request):
        subject_id = request.POST.get('subject_id')
        ordering = request.POST.get('ordering')
        title = request.POST.get('title')
        limit_hour = request.POST.get('limit_hour')
        desc = request.POST.get('desc')

        form = ExamForm({'subject': int(subject_id), 'ordering': int(ordering), 'title': title, 'limit_hour': limit_hour, 'desc': desc})
        if form.is_valid():
            form.save()

        else:
            messages.error(request, form.errors)
        
        return redirect('exams:exam_schedule')


class ExamEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'exams/exam_edit.html'
    permission_required = ('users.change_customuser')
    success_url = reverse_lazy('exams:exam_schedule')


class ExamDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Exam
    template_name = 'exams/exam_delete.html'
    permission_required = ('users.delete_customuser')
    success_url = reverse_lazy('exams:exam_schedule')



class ExamGradesListView(ListView):
    template_name = 'exams/exam-grade.html'
    context_object_name = 'exam_results'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['exams'] = Exam.objects.all().order_by('-id')
        context['students'] = get_user_model().objects.filter(role=CustomUser.Role.STUDENT.value)
        return context

    def get_queryset(self):
        queryset = ExamResult.objects.all()
        search_name = self.request.GET.get('search_name')
        if search_name:
            queryset = queryset.filter(exam__subject__name__icontains=search_name)

        search_percent = self.request.GET.get('search_percent')
        if search_percent:
            queryset = queryset.filter(percent__icontains=search_percent)
        return queryset

    def post(self, request):
        exam_id = request.POST.get('exam_id')
        student_id = request.POST.get('student_id')
        percent = request.POST.get('percent')
        comment = request.POST.get('comment')
        print(percent)

        form = ExamResultForm({'exam':exam_id, 'student':student_id, 'percent':percent, 'comment':comment})

        if form.is_valid():
            form.save()
        
        else:
            print(form.errors)
            messages.error(request, form.errors)

        return redirect('exams:exam_grade')


class ExamResultDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ExamResult
    template_name = 'exams/exam_delete.html'
    permission_required = ('users.delete_customuser')
    success_url = reverse_lazy('exams:exam_grade')
