from apps.notices.models import Message
from django.db.models import Q


def general(request):
    user_messages = Message.objects.filter(Q(chat__sender_id=request.user.id) |
                                           Q(chat__recipient_id=request.user.id)).select_related('chat').order_by('-created_at')[0:5]
    return {'user_messages': user_messages}