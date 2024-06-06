from django.urls import path
from .views import (StudentListView, TeacherListView, StudentDetailView, 
                    TeacherDetailView, ParentListView, ParentDetailView, error_403)


urlpatterns = [
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('teacher_list/', TeacherListView.as_view(), name='teacher_list'),
    path('student_detail/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('teacher_detail/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('parent_list/', ParentListView.as_view(), name='parent_list'),
    path('parent_detail/<int:pk>/', ParentDetailView.as_view(), name='parent_detail'),
    path('error_403/', error_403, name='error_403'),
]