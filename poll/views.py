from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from django.db.models import Count
from django.views.generic import CreateView, ListView, DetailView
from .form import PollForm
from .models import Poll, Option, Vote

# Create your views here.

def Home(req):
    return render(req, template_name='poll/home.html')


OptionFormSet = modelformset_factory(Option, fields=('text',), extra=0, can_delete=False)

class CreatePoll(CreateView):
    form_class = PollForm
    template_name =  "poll/create_poll.html"
    success_url = reverse_lazy('home')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = OptionFormSet(self.request.POST)
        else:
            context['formset'] = OptionFormSet(queryset=Option.objects.none())
        return context


    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            
            form.instance.created_by = self.request.user
            self.object = form.save()

            options = formset.save(commit=False)
            for option in options:
                option.poll = self.object  # attach poll FK
                option.save()

            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))

class PollListView(ListView):
    model = Poll
    template_name = "poll/poll_list.html"
    context_object_name = "polls"
    ordering = ['-created_at']


class PollDetailView(DetailView):
    model = Poll
    template_name = "poll/poll_detail.html"
    context_object_name = "poll"


class PollResultView(DetailView):
    model = Poll
    template_name = "poll/poll_result.html"
    context_object_name = "poll"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = self.object

        total_votes = Vote.objects.filter(option__poll=poll).count()
        options = poll.option_set.annotate(vote_count=Count("vote"))

        for option in options:
            option.percent = round((option.vote_count / total_votes) * 100) if total_votes else 0

        context["options"] = options
        context["total_votes"] = total_votes
        return context

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    
    if request.method == "POST":
        option_id = request.POST.get("choice")
        print(poll,"--- ", option_id)

        option = get_object_or_404(Option, pk=option_id, poll=poll)

        # prevent multiple votes per user per poll
        if Vote.objects.filter(user=request.user, option__poll=poll).exists():
            return redirect('poll_detail', pk=poll_id)

        Vote.objects.create(user=request.user, option=option)
        return redirect('poll_detail', pk=poll_id)

