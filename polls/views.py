from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Poll, Choice
from django.views.generic import TemplateView, ListView, DetailView

'''
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})
'''

class PollView(ListView):
    #используемая модель
    model = Poll
    #имя, используемое в шаблоне
    context_object_name='latest_poll_list'
    
    template_name='polls/index.html'
    
    #стандартная ф-ция для передачи в шаблон доп. параметров
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PollView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['poll_list'] = Poll.objects.order_by('-pub_date')[:3]
        return context

class PollDetailView(DetailView):
    model=Poll
    template_name='polls/detail.html'

'''
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response(  'polls/detail.html', 
                                {'poll': p},
                                context_instance=RequestContext(request))
'''
'''
#Длинный способ получения доступа к объекту из БД
try:
    p = Poll.objects.get(pk=poll_id)
except Poll.DoesNotExist:
    raise Http404
'''

class PollResultsView(DetailView):
    model=Poll
    template_name='polls/results.html'

'''
def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})
'''

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect('../results')
