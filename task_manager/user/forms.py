from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserEditForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
                                     attrs=
                                     {'placeholder': 'Имя'}),
                                 max_length=30, required=True,
                                 label='Имя',
                                 label_suffix='')
    last_name = forms.CharField(widget=forms.TextInput(
                                     attrs=
                                     {'placeholder': 'Фамилия'}),
                                max_length=30, required=True,
                                label='Фамилия',
                                label_suffix='',)
    username = forms.CharField(widget=forms.TextInput(
                                    attrs=
                                    {'placeholder': _('username_placeholder')}),
                               label=_('username_placeholder'),
                               label_suffix='',)
    password1 = forms.CharField(widget=forms.PasswordInput(
                                    attrs=
                                    {'placeholder': _('password')}),
                                label=_('password'),
                                label_suffix='',)
    password2 = forms.CharField(widget=forms.PasswordInput(
                                    attrs=
                                    {'placeholder': _('Подтверждение пароля')}),
                                label=_('Подтверждение пароля'),
                                label_suffix='')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password1',
                  'password2']
