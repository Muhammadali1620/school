from django.urls import path
from . import views

app_name = 'student_groups'


urlpatterns = [
    path('', views.GroupListView.as_view(), name='group_list-page'),
    path('create', views.StudentGroupCreateView.as_view(), name='group_create-page'),
    path('delete/<int:pk>', views.StudentGroupDeleteView.as_view(), name='group_delete-page'),
    path('update/<int:pk>', views.StudentGroupUpdateView.as_view(), name='group_update-page'),
    path('detail/<int:pk>', views.GroupDetailView.as_view(), name='group_detail-page'),
]
