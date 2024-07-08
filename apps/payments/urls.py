from django.urls import path
from . import views

app_name = 'payments'


urlpatterns = [
    path('', views.PaymentListView.as_view(), name='list_payment'),
    path('add/', views.PaymentCreateView.as_view(), name='add_payment'),
    path('<int:pk>/update/', views.PaymentUpdateView.as_view(), name='update_payment'),
    path('<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='delete_payment'),
]