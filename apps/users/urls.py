from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Students
    path('student_list/', views.StudentListView.as_view(), name='student_list'),
    path('student_detail/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('add_student/', views.StudentRegisterView.as_view(), name='add_student'),
    path('change_student/<int:pk>/', views.StudentUpdateView.as_view(), name='change_student'),
    path('search_student/', views.SearchStudentView.as_view(), name='search_student'),
    path('student_dashboard/', views.StudentDashboardView.as_view(), name='student_dashboard'),

    #Parents
    path('parent_list/', views.ParentListView.as_view(), name='parent_list'),
    path('change_parent/<int:pk>/', views.ParentUpdateView.as_view(), name='change_parent'),
    path('parent_detail/<int:pk>/', views.ParentDetailView.as_view(), name='parent_detail'),
    path('add_parent/', views.ParentRegisterView.as_view(), name='add_parent'),
    path('parent_dashboard/', views.ParentDashboardView.as_view(), name='parent_dashboard'),

    # Teachers
    path('teacher_list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('change_teacher/<int:pk>/', views.TeacherUpdateView.as_view(), name='change_teacher'),
    path('teacher_detail/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('add_teacher/', views.TeacherRegisterView.as_view(), name='add_teacher'),
    path('teacher_dashboard/', views.TeacherDashboardView.as_view(), name='teacher_dashboard'),
        
    # Account settings
    path('account_settings', views.AccountSettings.as_view(), name='account_settings'),
    path('delete_user/<int:pk>/', views.UserDeleteView.as_view(), name='delete_user'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/teacher/', views.TeacherRegisterView.as_view(), name='register_teacher'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

    #errors
    path('error_403/', views.error_403, name='error_403'),
]