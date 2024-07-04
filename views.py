from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.payments.models import Payment


class PaymentListView(ListView):
    template_name = 'all-fees.html'

    def get_queryset(self):
        queryset = Payment.objects.all()
        search_id = self.request.GET.get('search_id')
        search_name = self.request.GET.get('search_name')
        search_phone_number = self.request.GET.get('search_phone_number')

        if search_id:
            queryset = queryset.filter(id__startswith=search_id)

        if search_name:
            queryset = queryset.filter(
                Q(Q(student__first_name__icontains=search_name)
                  |
                  Q(student__last_name__icontains=search_name))
                |
                Q(Q(teacher__first_name__icontains=search_name)
                  |
                  Q(teacher__last_name__icontains=search_name)
                  )
            )
        if search_phone_number:
            queryset = queryset.filter(Q(student__phone_number__endswith=search_phone_number)
                                       |
                                       Q(teacher__phone_number__endswith=search_phone_number))
        return queryset


class PaymentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Payment
    fields = ['teacher', 'student', 'year', 'month', 'salary', 'in_percent', ]

    template_name = 'admit-form.html'
    permission_required = ('payments.add_payment',)
    success_url = reverse_lazy('payments_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New Payment'
        return context


class PaymentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Payment
    template_name = 'users_delete.html'
    permission_required = ('payments.delete_payment',)
    success_url = reverse_lazy('payments_list-page')


class PaymentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Payment
    fields = ['teacher', 'student', 'year', 'month', 'salary', 'in_percent', ]
    template_name = 'users_update.html'
    permission_required = ('payments.change_payment',)
    success_url = reverse_lazy('payments_list-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_new_object'] = 'Add New Payment'
        return context
