from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django.utils.translation import gettext_lazy as _


class PlaceholderAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={'placeholder': _('username_placeholder'),
                                'autofocus': True}),
        label=_('username_placeholder'),
        label_suffix=''
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={'placeholder': _('password_placeholder')}),
        label=_('password_placeholder'),
        label_suffix=''
    )
