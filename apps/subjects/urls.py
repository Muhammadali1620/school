from django.urls import path
from . import views

app_name = 'subjects'

urlpatterns = [
    path('subject_list/', views.SubjectTemplateView.as_view(), name='subject_list'),
]