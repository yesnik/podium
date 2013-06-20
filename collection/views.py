# -*- coding: utf-8 -*-

from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404

from collection.models import Vuz, Collection, Author, Prizer, Contest
from contest.models import Winner


class CollectionVuzListView(ListView):
    """
    Список коллекций по отдельному вузу
    """
    model = Collection
    context_object_name = 'collection_list'
    template_name = 'collection/collection_list.html'

    def get_queryset(self):
        vuz = self.kwargs['vuz']
        return Collection.objects.filter(author__vuz__vuz_url=vuz)


class CollectionNominationListView(ListView):
    """
    Список коллекций по конкретной номинации
    """
    model = Collection
    context_object_name = 'collection_list'
    template_name = 'collection/collection_list.html'

    def get_queryset(self):
        nomination = self.kwargs['nomination_url']
        return Collection.objects.filter(nomination__nomination_url=nomination)


class CollectionYearListView(ListView):
    """
    Список коллекций определенного года
    """
    context_object_name='collection_list'
    template_name='collection/collection_list.html'

    show_active_year = False
    other_years_list = []

    def get_queryset(self):
        # Показываем участников конкурса текущего года
        if self.show_active_year:
            # Вызываем метод модели, чтобы определить активный год
            year = Contest.get_active_year()
            collections = Collection.objects.filter(contest__year=year)
        else:
            year = self.kwargs['year']
            collections = Collection.objects.filter(contest__year=year)

        years_list = Contest.get_years()

        try:
            years_list.remove(int(year))
        except ValueError:
            pass

        self.other_years_list = years_list

        return collections

    def get_context_data(self, *args, **kwargs):
        context = super(CollectionYearListView, self).get_context_data(**kwargs)
        try:
            context['year'] = self.kwargs['year']
        except KeyError:
            pass
            
        context['other_years_list'] = self.other_years_list
        return context


class CollectionYearVuzListView(ListView):
    """
    Список коллекций вуза для определенного года
    """
    context_object_name = 'collection_list'
    template_name = 'collection/collection_list.html'

    show_active_year = False
    other_years_list = []

    def get_queryset(self):
        # Показываем участников конкурса текущего года
        if self.show_active_year:
            # Вызываем метод модели, чтобы определить активный год
            year = Contest.get_active_year()
            collections = Collection.objects.filter(contest__year=year, author__vuz__vuz_url=self.kwargs['vuz'])
        else:
            year = self.kwargs['year']
            collections = Collection.objects.filter(contest__year=year, author__vuz__vuz_url=self.kwargs['vuz'])

        years_list = Contest.get_years()

        try:
            years_list.remove(int(year))
        except ValueError:
            pass

        self.other_years_list = years_list

        return collections

    def get_context_data(self, *args, **kwargs):
        context = super(CollectionYearVuzListView, self).get_context_data(**kwargs)
        try:
            context['year'] = self.kwargs['year']
        except KeyError:
            pass

        context['vuz'] = self.kwargs['vuz']
        context['vuz_name'] = get_object_or_404(Vuz, vuz_url=self.kwargs['vuz']).name_short


        context['other_vuz_years_list'] = self.other_years_list
        return context



class AuthorDetailView(DetailView):
    """
    Подробный просмотр информации об авторе
    """
    model=Author
    template_name='collection/author_detail.html'
    context_object_name = 'author'

    def get_context_data(self, *args, **kwargs):
        author_id = self.kwargs['pk']
        author_collection = Collection.objects.filter(author__id = author_id)
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['author_collection_list'] = author_collection
        return context


class PrizerLastYearListView(ListView):
    """
    Список победителей последнего прошедшего конкурса
    """
    model = Prizer
    context_object_name='prizer_list'
    template_name='collection/prizer_list.html'

    def get_context_data(self, *args, **kwargs):
        years_list = [item['year'] for item in Contest.objects.values('year').order_by('-year')]
        
        try:
            prizer_year_list = Prizer.objects.filter(contest__year=years_list[0]).order_by('place')
        except:
            prizer_year_list = []

        try:
            winner_year_list = Winner.objects.filter(contest__year=years_list[0])
            print winner_year_list
        except:
            winner_year_list = []

        context = super(PrizerLastYearListView, self).get_context_data(**kwargs)
        context['prizer_year_list'] = prizer_year_list
        context['winner_year_list'] = winner_year_list
        context['years_list'] = years_list[1:]

        return context


class PrizerYearListView(ListView):
    """
    Список победителей конкурса определенного года
    """
    model = Prizer
    context_object_name='prizer_list'
    template_name='collection/prizer_year_list.html'

    def get_context_data(self, *args, **kwargs):
        
        year = self.kwargs['year']

        # Список коллекций-призеров данного года
        prizer_year_list = Prizer.objects.filter(contest__year=year).order_by('place')

        # Список победителей конкурса данного года - Мисс и Мистер подиум
        winner_year_list = Winner.objects.filter(contest__year=year)

        context = super(PrizerYearListView, self).get_context_data(**kwargs)
        context['prizer_year_list'] = prizer_year_list
        context['winner_year_list'] = winner_year_list

        return context
