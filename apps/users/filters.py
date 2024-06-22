import django_filters
from .models import CustomUser


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = ['gender', 'student_group']


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = ['gender', 'subject']
