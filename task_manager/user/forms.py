from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserEditForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,
                                 label='Имя')
    last_name = forms.CharField(max_length=30, required=True,
                                label='Фамилия')
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label=_('password'))
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label=_('confirm password'))

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password1',
                  'password2']
