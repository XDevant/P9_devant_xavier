from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
                                    'placeholder': 'SuperDupond42',
                                    })
        self.fields['password1'].widget.attrs.update({
                                    'placeholder': '8 caractères min',
                                    })
        self.fields['password2'].widget.attrs.update({
                                    'placeholder': '8 caractères min',
                                    })


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=63,
        label='Nom d’utilisateur',
        widget=forms.TextInput(attrs={'placeholder': 'SuperDupond42'})
        )
    password = forms.CharField(
        max_length=63,
        widget=forms.PasswordInput(attrs={'placeholder': '********'}),
        label='Mot de passe'
        )
