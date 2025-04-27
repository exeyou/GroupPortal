from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Poll, Vote
from .forms import VoteForm


def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'vote/poll_list.html', {'polls': polls})


@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    try:
        existing_vote = Vote.objects.get(user=request.user, poll=poll)
    except Vote.DoesNotExist:
        existing_vote = None

    if request.method == 'POST':
        form = VoteForm(poll, request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            # переголосування
            if existing_vote:
                existing_vote.choice = choice
                existing_vote.save()
            else:
                Vote.objects.create(user=request.user, poll=poll, choice=choice)
            return redirect('vote:poll_results', poll_id=poll.id)
    else:
        form = VoteForm(poll)

    return render(request, 'vote/poll_detail.html', {'poll': poll, 'form': form, 'existing_vote': existing_vote})


def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    choices = poll.choices.all()
    total_votes = Vote.objects.filter(poll=poll).count()
    return render(request, 'vote/poll_results.html', {
        'poll': poll,
        'choices': choices,
        'total_votes': total_votes
    })
