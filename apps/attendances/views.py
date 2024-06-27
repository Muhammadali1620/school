import calendar
from django.views.generic import ListView
from apps.attendances.models import Attendance
from apps.groups.models import StudentGroup
from datetime import date
from apps.users.models import CustomUser


class AttendanceListView(ListView):
    template_name = "student-attendance.html"
    context_object_name = 'attendances'
    extra_context = {
        'groups': StudentGroup.objects.all().select_related('subject').order_by('subject__name'),
    }

    def get_queryset(self):
        group_id = self.request.GET.get('group_id', '')
        year = self.request.GET.get('year', '')
        month = self.request.GET.get('month', '')
        if len(list(filter(str.isdigit, [group_id, month, year]))) != 3 or len(list(filter(str.isdigit, [group_id, month, year]))) == '':
            queryset = Attendance.objects.none()
        else:
            queryset = Attendance.objects.all().filter(student__student_group_id=group_id,
                                                       date__month=month,
                                                       date__year=year).order_by('date__day')
        return queryset

    def get_context_data(self, **kwargs):
        group_id = self.request.GET.get('group_id', '')
        year = self.request.GET.get('year', '')
        month = self.request.GET.get('month', '')

        context = super().get_context_data(**kwargs)
        today = date.today()
        context['years'] = list(range(2024, today.year + 11))

        if group_id.isdigit():
            context['students'] = CustomUser.objects.filter(student_group_id=group_id, role=CustomUser.Role.STUDENT.value).prefetch_related('student_attendance').order_by('first_name')
        else:
            context['students'] = []

        if month.isdigit() and year.isdigit():
            context['months'] = list(range(1, calendar.monthrange(int(year), int(month))[1] + 1))
        else:
            context['months'] = []

        return context
