from django.forms import ModelForm
from apps.exams.models import Exam, ExamResult


class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['subject', 'title', 'desc', 'ordering', 'limit_hour']


class ExamResultForm(ModelForm):
    class Meta:
        model = ExamResult
        fields = '__all__'