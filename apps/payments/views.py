from django.shortcuts import render
from django.views.generic import TemplateView


class FeesCollectionTemplateView(TemplateView):
    template_name = "all-fees.html"


class ExpenseTemplateView(TemplateView):
    template_name = "all-expense.html"


class AddExpenseTemplateView(TemplateView):
    template_name = "add-expense.html"