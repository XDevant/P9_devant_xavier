from itertools import chain
from unicodedata import name
from django.db import IntegrityError
from django.db.models import BooleanField, CharField, Value, Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from review.models import Ticket,Review, UserFollows
from authentication.models import User


@login_required
def flux(request):
    flux_owner = request.user
    owner_followeds = UserFollows.objects.filter(user = flux_owner)
    followed = [user.followed_user for user in owner_followeds]

    reviews = Review.objects.filter(Q(user__in=followed) | Q(user=flux_owner))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = Ticket.objects.filter(Q(user__in=followed) | Q(user=flux_owner))
    tickets = tickets.annotate(
                               content_type=Value('TICKET', CharField()),
                               answered=Value(False, BooleanField())
                               )
    for ticket in tickets:
        answered = Review.objects.filter(ticket=ticket, user=flux_owner)
        if len(answered) > 0:
            ticket.answered = True
    posts = sorted(chain(reviews, tickets), 
                   key=lambda post: post.time_created, 
                   reverse=True)
    return render(request, 'review/flux.html', context={'posts': posts})

@login_required
def posts(request):
    current_user = request.user
    reviews = Review.objects.filter(user=current_user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = Ticket.objects.filter(user=current_user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    posts = sorted(chain(reviews, tickets), 
                   key=lambda post: post.time_created, 
                   reverse=True)
    return render(request, 'review/posts.html', context={'posts': posts})

@login_required
def followed(request):
    """"""
    current_user = request.user
    followers = UserFollows.objects.filter(followed_user=current_user)
    followers = [follower.user for follower in followers]
    followeds = UserFollows.objects.filter(user=current_user)
    followeds = [followed.followed_user for followed in followeds]
    form = forms.FollowForm()
    context = {'form': form,'followers': followers, 'followeds': followeds}
    context["message"] = ""
    if request.method == 'POST':
        follow = UserFollows()
        follow.user = request.user
        if 'follow' in request.POST:
            form = forms.FollowForm(request.POST)
            username=request.POST['name']
            if username == str(current_user):
                context["message"] = "Vous vous suivez déjà vous même!"
            if form.is_valid() and username != str(current_user):
                try:
                    follow.followed_user = User.objects.get(username=username)
                except User.DoesNotExist:
                    context["message"] = f"{username} n'existe pas!"
                else:
                    try:
                        follow.save()
                        return redirect('followed')
                    except IntegrityError:
                        context["message"] = f"Vous suivez déja {username}."
            return render(request, 'review/followed.html', context=context)
        else:
            user=current_user.id
            followed=User.objects.get(username=request.POST['followed']).id
            follow = UserFollows.objects.filter(
                user=user,
                followed_user=followed
                )
            follow.delete()
            return redirect('followed')
    return render(request, 'review/followed.html', context=context)

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
    context = {'form': form}
    return render(request, 'review/create_ticket.html', context=context)

@login_required
def create_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
}
    return render(request, 'review/create_review.html', context=context)

@login_required
def ticket_review(request, id):
    ticket = Ticket.objects.get(id=id)
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')
    context={'ticket': ticket, 'form': form}
    return render(request, 'review/ticket_review.html', context=context)

@login_required
def edit_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('posts')
    else:
        form = forms.TicketForm(instance=ticket)
    return render(request, 'review/edit_ticket.html', {'form': form})

@login_required
def delete_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('posts')
    return render(request, 'review/delete_ticket.html', {'ticket': ticket})

@login_required
def edit_review(request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = forms.ReviewForm(instance=review)
    return render(request, 'review/edit_review.html', {'form': form})

@login_required
def delete_review(request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        review.delete()
        return redirect('posts')
    return render(request, 'review/delete_review.html', {'review': review})
