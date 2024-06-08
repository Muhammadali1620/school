from django.urls import path
from . import views

app_name = 'adittionals'


urlpatterns = [
    path('all_additional/', views.AdditionalTemplateView.as_view(), name='all_additional'),
    path('add_additional/', views.AddAdditionalTemplateView.as_view(), name='add_additional'),

]