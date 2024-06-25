from django.shortcuts import redirect
from apps.notices.forms import MessageForm
from apps.notices.models import Chat, Message
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class ChatListView(LoginRequiredMixin, ListView):
    queryset = Chat.objects.all()
    template_name = 'chat/chat.html'
    context_object_name = 'chats'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chat_id = self.request.GET.get('chat_id')
        if chat_id:
            context['chat_messages'] = Message.objects.filter(chat_id=chat_id).select_related('chat').order_by('created_at')
        else:
            context['chat_messages'] = None
        return context

    def get_queryset(self):
        user = self.request.user
        self.queryset = self.queryset.filter(Q(sender_id=user.pk) | Q(recipient_id=user.pk)).select_related('sender', 'recipient').prefetch_related('messages')
        query = self.request.GET.get('query')
        if query:
            self.queryset = self.queryset.filter(Q(sender__first_name__icontains=query) |
                                                 Q(sender__last_name__icontains=query) |
                                                 Q(recipient__first_name__icontains=query) |
                                                 Q(recipient__last_name__icontains=query))
        return self.queryset
    
    def post(self, request, *args, **options):
        chat_id = request.GET.get('chat_id')
        content = request.POST.get('content')
        if chat_id and content:
            form = MessageForm({'chat': int(chat_id), 'content': content, 'sender': request.user.pk})
            if form.is_valid():
                form.save()
            else:
                messages.error(request, 'Invalid form data')
        else:
            messages.error(request, 'Invalid request')
        return redirect(request.META['HTTP_REFERER'])


class NotificationTemplateView(TemplateView):
    template_name = 'notice-board.html'