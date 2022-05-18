from django import forms
from . import models
from .widgets import StarRatingWidget, ImageWidget


class TicketForm(forms.ModelForm):
    """ """
    class Meta:
        model = models.Ticket
        fields = ('title', 'description', 'image')
        labels = {'title': 'Titre'}
        widgets = {'image': ImageWidget()}


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        labels = {
                 'headline': 'Titre',
                 'rating': 'Note',
                 'body': 'Commentaire'
                 }
        widgets = {
                  'rating': StarRatingWidget()
                  }


class FollowForm(forms.Form):
    """We add the follow tag to filter our post requests in view"""
    follow = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    name = forms.CharField(max_length=8192)
