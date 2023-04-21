from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Module


class Home(ListView):
    model = Module
    template_name = 'app/index.html'
    context_object_name = 'modules'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Образовательные модули'
        return context


class GetModule(DetailView):
    model = Module
    template_name = 'app/module.html'
    context_object_name = 'module'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Образовательный модуль: '
        return context