from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


class StudentGroupTemplateView(TemplateView):
    template_name = 'all-class.html'


class AddStudentGroupTemplateView(TemplateView):
    template_name = 'add-class.html'


def set_language(request, lang):
    current_lang = request.GET.get('current_lang', 'en')
    print(current_lang)
    next_url = request.META['HTTP_REFERER']
    next_url = str(next_url).replace(current_lang, lang, 1)
    return HttpResponseRedirect(next_url)


def home(request):
    lang = request.GET.get('language')
    context = {
        'salomlar': ['hello', 'rivet'],
        'lang': lang
    }
    return render(request, template_name='index.html', context=context)