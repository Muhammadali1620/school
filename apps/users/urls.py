from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('student_list/', views.StudentListView.as_view(), name='student_list'),
    path('account_settings', views.AccountSettingsView.as_view(), name='account_settings'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/teacher/', views.TeacherRegisterView.as_view(), name='register_teacher'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'), 
    path('teacher_list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('student_detail/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('teacher_detail/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('parent_list/', views.ParentListView.as_view(), name='parent_list'),
    path('parent_detail/<int:pk>/', views.ParentDetailView.as_view(), name='parent_detail'),
    path('error_403/', views.error_403, name='error_403'),
]