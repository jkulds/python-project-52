from django import forms

from django.utils.translation import gettext_lazy as _

from task_manager.models import TaskModel


class TaskModelForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150, required=True, label=_('Имя'),
        widget=forms.TextInput(attrs={'placeholder': _('Имя')}),
    )
    description = forms.CharField(
        max_length=150, required=True, label=_('Описание'),
        widget=forms.Textarea(attrs={'placeholder': _('Описание')}),
    )

    class Meta:
        model = TaskModel
        fields = ['name', 'description', 'executor', 'status', 'labels']
