from django import forms
from apps.notices.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['chat', 'sender', 'content']