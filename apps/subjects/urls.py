from django.urls import path
from . import views

app_name = 'subjects'

urlpatterns = [
    path('subject/', views.SubjectListView.as_view(), name='subject_page'),
    path('subject-delete/<int:pk>/', views.SubjectDeleteView.as_view(), name='subject_delete'),
    path('subject-edit/<int:pk>/', views.SubjectEditView.as_view(), name='subject_edit'),
]