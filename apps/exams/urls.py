from django.urls import path
from . import views

app_name = 'exams'

urlpatterns = [
    path('exam_schedule/', views.ExamScheduleTemplateView.as_view(), name='exam_schedule'),
    path('exam_grade/', views.ExamScheduleTemplateView.as_view(), name='exam_grade'),
]