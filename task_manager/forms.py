from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.utils.safestring import mark_safe

from django.utils.translation import gettext_lazy as _
from django.forms import BaseForm


orig_init = BaseForm.__init__


def BaseForm_init(*args, **kwargs):
    kwargs.setdefault("label_suffix", mark_safe(''))
    orig_init(*args, **kwargs)


BaseForm.__init__ = BaseForm_init


class PlaceholderAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={'placeholder': _('username_placeholder'),
                                'autofocus': True}),
        label=_('username_placeholder')
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={'placeholder': _('password_placeholder')}),
        label=_('password_placeholder')
    )
