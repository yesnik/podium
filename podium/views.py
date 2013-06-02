# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist

from page.models import Page
from statictxt.models import StaticText


class PageView(TemplateView):
    """
    Страница со вставками статичных элементов
    """
    template_name='page/page_detail.html'
    context_object_name = 'page'

    def get_context_data(self, **kwargs):

        context = super(PageView, self).get_context_data(**kwargs)

        try:
            page = Page.objects.get(page_url='main')
            context['page'] = page
        except ObjectDoesNotExist:
            context['page'] = {'content':'Страница не найдена'}
            
        try:
            context['sidebar'] = StaticText.objects.get(alias = 'sidebar')
        except ObjectDoesNotExist:
            context['sidebar'] = {'content':'Define sidebar, please...'}
            
        try:
            context['footer'] = StaticText.objects.get(alias = 'footer')
        except ObjectDoesNotExist:
            context['footer'] = {'content':'Define footer, please...'}

        return context