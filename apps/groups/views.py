from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class StudentGroupTemplateView(TemplateView):
    template_name = 'all-class.html'


class AddStudentGroupTemplateView(TemplateView):
    template_name = 'add-class.html'


def set_language(request):
    language_code = request.POST.get('language', 'uz')
    return redirect(request.META["HTTP_ORIGIN"] + f'/{language_code}/')


def home(request):
    lang = request.GET.get('language')
    context = {
        'salomlar': ['hello', 'rivet'],
        'lang': lang
    }
    return render(request, template_name='index.html', context=context)