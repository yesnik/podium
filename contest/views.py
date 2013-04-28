from django.views.generic import DetailView, ListView
from contest.models import Jury, Contest


class JuryContestListView(ListView):
    """
    Список жюри конкретного конкурса
    """
    model = Jury
    context_object_name = 'jury_list'
    template_name = 'contest/jury_year_list.html'

    def get_queryset(self):
        year = self.kwargs['year']
        return Jury.objects.filter(contest__year=year)

    def get_context_data(self, *args, **kwargs):
        context = super(JuryContestListView, self).get_context_data(**kwargs)
        context['year'] = self.kwargs['year']
        return context


class JuryYearsListView(ListView):
    """
    Список жюри по годам
    """
    model = Jury
    context_object_name='jury_list'
    template_name='contest/jury_list.html'

    def get_context_data(self, *args, **kwargs):
        years = Contest.objects.values('year').order_by('-year')
        jury_full_list = Jury.objects.all()
        jury_year_list = []

        for item in years:
            year = item['year']
            dict_item = {'year': year, 'jury_list': jury_full_list.filter(contest__year=year)}
            jury_year_list.append(dict_item)

        context = super(JuryYearsListView, self).get_context_data(**kwargs)
        context['jury_year_list'] = jury_year_list
        return context