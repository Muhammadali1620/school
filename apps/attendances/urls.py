from django.urls import path
from . import views

app_name = 'attendances'

urlpatterns = [
    path('student_attendance/', views.StudentAttendanceTemplateView.as_view(), name='student_attendance'),
]