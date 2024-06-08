from django.urls import path
from . import views

app_name = 'payments'


urlpatterns = [
    path('all_fees/', views.FeesCollectionTemplateView.as_view(), name='all_fees'),
    path('all_expense/', views.ExpenseTemplateView.as_view(), name='all_expense'),
    path('add_expense/', views.AddExpenseTemplateView.as_view(), name='add_expense'),
]