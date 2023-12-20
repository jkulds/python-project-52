from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.models import TaskStatus


class TaskStatusForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('Имя')}),
        label=_('Имя'),
        label_suffix='')

    class Meta:
        model = TaskStatus
        fields = ['name']
