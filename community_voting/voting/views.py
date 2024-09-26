from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Issue, Vote

def issue_list(request):
    issues = Issue.objects.filter(is_open=True)
    return render(request, 'voting/issue_list.html', {'issues': issues})

@login_required
def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, 'voting/issue_detail.html', {'issue': issue})

@login_required
def vote(request, pk, vote_value):
    issue = get_object_or_404(Issue, pk=pk)
    vote, created = Vote.objects.get_or_create(user=request.user, issue=issue)
    if created or vote.vote_value != vote_value:
        vote.vote_value = vote_value
        vote.save()
    return redirect('issue_detail', pk=issue.pk)

def issue_results(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    total_votes = Vote.objects.filter(issue=issue).count()
    yes_votes = Vote.objects.filter(issue=issue, vote_value=True).count()
    no_votes = total_votes - yes_votes
    return render(request, 'voting/issue_results.html', {
        'issue': issue,
        'total_votes': total_votes,
        'yes_votes': yes_votes,
        'no_votes': no_votes
    })
