# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView, DetailView
from django.core.exceptions import ObjectDoesNotExist

from page.models import *
from statictxt.models import *


class PageDetailView(TemplateView):
    model = Page
    template_name = 'page/page_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)

        try:
            context['sidebar'] = StaticText.objects.get(alias='sidebar')
        except ObjectDoesNotExist:
            context['sidebar'] = {'content':'Define sidebar, please...'}

        page = Page.objects.get(page_url=self.kwargs['page_url'])
        
        context['page'] = page
            
        try:
            context['footer'] = StaticText.objects.get(alias='footer')
        except ObjectDoesNotExist:
            context['footer'] = {'content':'Define footer, please...'}

        return context