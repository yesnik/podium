from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from blog.models import *
from statictxt.models import *
from django.views.generic import TemplateView, ListView, DetailView
from pics.models import Pic
from persons.models import Person

from django.core.exceptions import ObjectDoesNotExist


class PageListView(ListView):
    #используемая модель
    model = Page

class PageView(DetailView):
    model=Page
    template_name='blog/detail.html'

    #стандартная ф-ция для передачи в шаблон доп. параметров
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PageView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['menu'] = Page.objects.all()
        try:
            context['sidebar'] = StaticText.objects.get(alias = 'sidebar')
        except ObjectDoesNotExist:
            context['sidebar'] = {'content':'Define sidebar, please...'}
            
        try:
            context['footer'] = StaticText.objects.get(alias = 'footer')
        except ObjectDoesNotExist:
            context['footer'] = {'content':'Define footer, please...'}
            
        try:
            context['persons'] = Person.objects.filter(page_id = self.kwargs['pk'])
        except ObjectDoesNotExist:
            context['persons'] = {'fio':'Define person for this page.'}
            
        context['images'] = Pic.objects.filter(page_id = self.kwargs['pk'])
        return context