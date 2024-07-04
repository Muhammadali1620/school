from django.urls import path
from . import views

app_name = 'payments'


urlpatterns = [
    path('', views.PaymentListView.as_view(), name='payment_list'),
    path('add/', views.PaymentCreateView.as_view(), name='add_payment'),
    path('add_expense/', views.AddExpenseTemplateView.as_view(), name='add_expense'),
    path('teacher_payment_list/', views.TeacherAllPayments.as_view(), name='teacher_payment_list'),
]