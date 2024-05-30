from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from apps.lessons.models import Lesson
from apps.subjects.models import Subject


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

# class HomeView(View):

#     def get(self, request):
#         return HttpResponse('salom')
    
#     def post(self, request):
#         return render(request, template_name='index.html')
    

class HomeTemplateView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'salomlar': ['hello', 'rivet'],
        'asd':12,
        'subjects': Subject.objects.all()
    }

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['lang'] = self.request.GET.get('language')
        return context
    

class SubjectListView(ListView):
    paginate_by = 3
    page_kwarg = 'salom'
    queryset = Subject.objects.all()
    extra_context = {
        'lessons': Lesson.objects.all()
    }

    def get_queryset(self) -> QuerySet[Any]:
        category_id = self.request.GET.get('category_id')
        return self.queryset.filter()
    

class SubjectDetailView(DetailView):
    model = Subject
    # context_object_name = 'sub'
    pk_url_kwarg = 'subject_id'
    query_pk_and_slug = 'pk'

    # def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
    #     print(self.request.user)
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     return Subject.objects.filter(user_id=user.pk, pk=1)