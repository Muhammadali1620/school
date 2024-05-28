from django.shortcuts import render, redirect
from apps.subjects.models import Subject


def set_language(request):
    language_code = request.POST.get('language', 'uz')
    return redirect(request.META["HTTP_ORIGIN"] + f'/{language_code}/')


def home(request):
    return render(request, template_name='index.html', context={'subs': Subject.objects.all()})