from django.urls import path
from . import views

app_name = 'exams'

urlpatterns = [
    path('exam-schedule/', views.ExamScheduleListView.as_view(), name='exam_schedule'),
    path('exam-edit/<int:pk>/', views.ExamEditView.as_view(), name='exam_edit'),
    path('exam-delete/<int:pk>/', views.ExamDeleteView.as_view(), name='exam_delete'),
    path('exam-grade/', views.ExamGradesListView.as_view(), name='exam_grade'),
    path('exam-result-delete/<int:pk>/', views.ExamResultDeleteView.as_view(), name='exam_result_delete')
]