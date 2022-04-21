from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

@login_required
def flux(request):
    return render(request, 'review/flux.html')

@login_required
def posts(request):
    return render(request, 'review/posts.html')

@login_required
def create_ticket(request):
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')
    return render(request, 'review/create_ticket.html', context={'form': form})

@login_required
def create_review(request):
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('flux')
    return render(request, 'review/create_review.html', context={'form': form})

@login_required
def create_post(request):
    return render(request, 'review/create_post.html')

@login_required
def followed(request):
    return render(request, 'review/followed.html')