from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
    path('message/', views.MessageTemplateView.as_view(), name='message'),
    path('notification/', views.NotificationTemplateView.as_view(), name='notification'),
]