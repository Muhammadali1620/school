from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Payment
from django.views.generic import TemplateView, ListView


class FeesCollectionTemplateView(TemplateView):
    template_name = "all-fees.html"


class ExpenseTemplateView(TemplateView):
    template_name = "all-expense.html"


class AddExpenseTemplateView(TemplateView):
    template_name = "add-expense.html"


class TeacherAllPayments(ListView):
    queryset = Payment.objects.filter(teacher__isnull=False).select_related('teacher', 'teacher__subject')
    template_name = "teacher-payment.html"
    context_object_name = 'payments'