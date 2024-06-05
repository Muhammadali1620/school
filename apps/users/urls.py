from django.urls import path
from .views import StudentListView, error_403

urlpatterns = [
    path('student_list/', StudentListView.as_view(), name='student_list'),
    path('error_403/', error_403, name='error_403'),
]