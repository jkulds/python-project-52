from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, \
    UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 required=True,
                                 help_text=_('required'))
    last_name = forms.CharField(max_length=30,
                                required=True,
                                help_text=_('required'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']


class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 help_text=_('required'))
    last_name = forms.CharField(max_length=30, required=True,
                                help_text=_('required'))
    password = forms.CharField(widget=forms.PasswordInput,
                               help_text=_('Enter password'))
    password2 = forms.CharField(widget=forms.PasswordInput,
                                help_text=_('Confirm password'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password',
                  'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['placeholder'] = _(
            'Enter new password')
        self.fields['password2'].widget.attrs['placeholder'] = _(
            'Confirm password')

