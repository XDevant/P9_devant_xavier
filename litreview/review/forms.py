from django import forms

from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']

class FollowForm(forms.Form):
    follow = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    name = forms.CharField(max_length=8192)