from django.views.generic import DetailView, ListView
from collection.models import Vuz, Collection, Author


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