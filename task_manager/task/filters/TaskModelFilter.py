from django import forms
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter

from task_manager.models import LabelModel, TaskModel


class TaskModelFilter(FilterSet):
    labels = ModelChoiceFilter(
        queryset=LabelModel.objects.all(),
        label=_('Label')
    )

    own_tasks = BooleanFilter(
        label=_('My tasks'),
        widget=forms.CheckboxInput,
        method='get_own_tasks',
    )

    def get_own_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = TaskModel()
        fields = ['status', 'assignee']