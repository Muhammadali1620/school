from modeltranslation.translator import TranslationOptions, register
from apps.lessons.models import Lesson


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'desc',)