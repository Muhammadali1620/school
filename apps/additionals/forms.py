from django.forms import ModelForm
from apps.additionals.models import AdditionalTask

class AdditionalTaskForm(ModelForm):
    class Meta:
        model = AdditionalTask
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'