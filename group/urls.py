from django.urls import path

from apps.groups.views import GroupListView, StudentGroupCreateView, StudentGroupDeleteView, StudentGroupUpdateView, GroupDetailView

urlpatterns = [
    path('', GroupListView.as_view(), name='group_list-page'),
    path('create', StudentGroupCreateView.as_view(), name='group_create-page'),
    path('delete/<int:pk>', StudentGroupDeleteView.as_view(), name='group_delete-page'),
    path('update/<int:pk>', StudentGroupUpdateView.as_view(), name='group_update-page'),
    path('detail/<int:pk>', GroupDetailView.as_view(), name='group_detail-page'),
]
