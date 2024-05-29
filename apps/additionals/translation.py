from modeltranslation.translator import TranslationOptions, register
from apps.additionals.models import AdditionalTask


@register(AdditionalTask)
class AdditionalTaskTranslationOptions(TranslationOptions):
    fields = ('title', 'desc',)