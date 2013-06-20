# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist

from page.models import Page
from statictxt.models import StaticText
from collection.models import Collection, Vuz, Author
from contest.models import Contest


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


class VuzYearListView(ListView):
    """
    Список вузов-участников определенного года
    """
    context_object_name='vuz_list'
    template_name='collection/vuz_list.html'

    def queryset(self):

        if 'year' not in self.kwargs:
            year = Contest.get_active_year()
        else:
            year = int(self.kwargs['year'])

        collections_year_list = Collection.objects.filter(contest__year=year)
        vuz_list = []

        for collection in collections_year_list:
            for author in collection.author.all():
                if author.vuz not in vuz_list:
                    vuz_list.append(author.vuz)

        return vuz_list

    def get_context_data(self, **kwargs):

        context = super(VuzYearListView, self).get_context_data(**kwargs)

        year_list = Contest.get_years()

        if 'year' in self.kwargs:
            year = int(self.kwargs['year'])
        else:
            year = Contest.get_active_year()
        #Удаляем текущий год из списка, т.к. он уже отображается на странице

        print type(year)

        if year in year_list:
            year_list.remove(year)

        context['year_list'] = year_list
        return context

        
        