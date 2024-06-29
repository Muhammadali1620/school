from django.urls import path
from . import views

app_name = 'adittionals'


urlpatterns = [
    path('', views.AdditionalListView.as_view(), name='all_additional'),
    path('add/', views.AddAdditionalCreateView.as_view(), name='add_additional'),
    path('<int:pk>/update/', views.AdditionalUpdateView.as_view(), name='update_additional'),
    path('<int:pk>/delete/', views.AdditionalDeleteView.as_view(), name='delete_additional'),

]