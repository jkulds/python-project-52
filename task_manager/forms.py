from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from django.utils.translation import gettext_lazy as _


class PlaceholderAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={'placeholder': _('Имя пользователя'),
                                'autofocus': True}),
        label=_('Имя пользователя'),
        label_suffix=''
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={'placeholder': _('Пароль')}),
        label=_('Пароль'),
        label_suffix=''
    )
