from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Students
    path('students/view/', views.StudentListView.as_view(), name='student_list'),
    path('student/<int:pk>/detail/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/register/', views.StudentRegisterView.as_view(), name='add_student'),
    path('student/<int:pk>/update/', views.StudentUpdateView.as_view(), name='change_student'),
    path('search_student/', views.SearchStudentView.as_view(), name='search_student'),
    path('student_dashboard/', views.StudentDashboardView.as_view(), name='student_dashboard'),

    #Parents
    path('parents/view/', views.ParentListView.as_view(), name='parent_list'),
    path('parent/<int:pk>/detail/', views.ParentDetailView.as_view(), name='parent_detail'),
    path('parent/register/', views.ParentRegisterView.as_view(), name='add_parent'),
    path('parent/<int:pk>/update/', views.ParentUpdateView.as_view(), name='change_parent'),
    path('parent_dashboard/', views.ParentDashboardView.as_view(), name='parent_dashboard'),

    # Teachers
    path('teachers/view/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher/<int:pk>/update/', views.TeacherUpdateView.as_view(), name='change_teacher'),
    path('teacher/<int:pk>/detail/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/register/', views.TeacherRegisterView.as_view(), name='add_teacher'),
    path('teacher_dashboard/', views.TeacherDashboardView.as_view(), name='teacher_dashboard'),
        
    # Account settings
    path('account_settings/', views.AccountSettings.as_view(), name='account_settings'),
    path('delete/<int:pk>/user/', views.UserDeleteView.as_view(), name='delete_user'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]