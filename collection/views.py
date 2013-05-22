from django.views.generic import DetailView, ListView
from collection.models import Vuz, Collection, Author, Prizer, Contest


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

        context = super(PrizerLastYearListView, self).get_context_data(**kwargs)
        context['prizer_year_list'] = prizer_year_list
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
        print year

        try:
            prizer_year_list = Prizer.objects.filter(contest__year=year).order_by('place')
        except:
            prizer_year_list = []

        context = super(PrizerYearListView, self).get_context_data(**kwargs)
        context['prizer_year_list'] = prizer_year_list

        return context
