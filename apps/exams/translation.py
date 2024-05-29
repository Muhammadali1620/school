from modeltranslation.translator import TranslationOptions, register
from apps.exams.models import Exam


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title', 'desc',)