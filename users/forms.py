from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser
from django.shortcuts import redirect


class SignupForm(UserCreationForm):
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput())

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'date_of_birth']
        help_texts = {
            'username': None,
            'email': None,
            'password2': None
        }
