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
    executor = forms.ChoiceField(label_suffix='', label='Исполнитель')
    status = forms.ChoiceField(label_suffix='', label='Стасус')
    labels = forms.MultipleChoiceField(label_suffix='', label='Метки')

    def __init__(self, *args, **kwargs):
        super(TaskModelForm, self).__init__(*args, **kwargs)
        empty_label = ('', '--------------')
        self.fields['executor'].choices = \
            [(x.id, x.first_name + ' ' + x.last_name) for x in User.objects.all()]
        self.fields['executor'].choices.insert(0, empty_label)

        self.fields['status'].choices = \
            [(x.id, x.name) for x in TaskStatus.objects.all()]
        self.fields['status'].choices.insert(0, empty_label)

        self.fields['labels'].choices = \
            [(x.id, x.name) for x in LabelModel.objects.all()]



    class Meta:
        model = TaskModel
        fields = ['name', 'description', 'executor', 'status', 'labels']
