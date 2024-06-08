from django.views.generic import TemplateView



class MessageTemplateView(TemplateView):
    template_name = 'messaging.html'


class NotificationTemplateView(TemplateView):
    template_name = 'notice-board.html'