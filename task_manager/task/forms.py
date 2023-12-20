from django import forms
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

from task_manager.models import TaskModel, TaskStatus, LabelModel


class TaskModelForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150, required=True, label=_('Имя'),
        widget=forms.TextInput(attrs={'placeholder': _('Имя')}),
        label_suffix=''
    )
    description = forms.CharField(
        max_length=150, required=False, label=_('Описание'),
        widget=forms.Textarea(attrs={'placeholder': _('Описание')}),
        label_suffix=''
    )
    executor = forms.ModelChoiceField(label_suffix='', label='Исполнитель',
                                      empty_label='-----------',
                                      queryset=User.objects.all(),
                                      required=False)
    status = forms.ModelChoiceField(label_suffix='', label='Статус',
                                    empty_label='-----------',
                                    queryset=TaskStatus.objects.all())
    labels = forms.ModelMultipleChoiceField(label_suffix='', label='Метки',
                                            queryset=LabelModel.objects.all(),
                                            required=False)

    class Meta:
        model = TaskModel
        fields = ['name', 'description', 'executor', 'status', 'labels']
