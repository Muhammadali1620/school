from django.urls import path
from . import views

app_name = 'student_groups'


urlpatterns = [
    path('all_group/', views.StudentGroupTemplateView.as_view(), name='all_group'),
    path('add_group/', views.AddStudentGroupTemplateView.as_view(), name='add_group'),
]