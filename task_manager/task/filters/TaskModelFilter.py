from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter

from task_manager.models import LabelModel, TaskModel, TaskStatus


class TaskModelFilter(FilterSet):
    labels = ModelChoiceFilter(
        queryset=LabelModel.objects.all(),
        label=_('Метка'),
        label_suffix='',
    )

    executor = ModelChoiceFilter(
        label_suffix='',
        label=_('Исполнитель'),
        queryset=User.objects.all())
    status = ModelChoiceFilter(
        label_suffix='',
        label=_('Статус'),
        queryset=TaskStatus.objects.all())

    own = BooleanFilter(
        label=_('Только свои задачи'),
        label_suffix='',
        widget=forms.CheckboxInput,
        method='filter_own',
    )

    def filter_own(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = TaskModel()
        fields = ['status', 'executor']
