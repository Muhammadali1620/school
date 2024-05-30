from django.urls import path
from .views import home, SubjectListView, SubjectDetailView

urlpatterns = [
    path('', SubjectListView.as_view(), name='home'),
    path('/detail/<int:subject_id>/', SubjectDetailView.as_view(), name='subject-detail'),
]