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


class PrizerYearsListView(ListView):
    """
    Список победителей по годам
    """
    model = Prizer
    context_object_name='prizer_list'
    template_name='collection/prizer_list.html'

    def get_context_data(self, *args, **kwargs):
        years = Contest.objects.values('year').order_by('-year')
        prizer_full_list = Prizer.objects.all()
        
        prizer_year_list = []

        for item in years:
            year = item['year']
            dict_item = {'year': year, 'prizer_list': prizer_full_list.filter(contest__year=year).order_by('place')}
            prizer_year_list.append(dict_item)

        context = super(PrizerYearsListView, self).get_context_data(**kwargs)
        context['prizer_year_list'] = prizer_year_list

        return context