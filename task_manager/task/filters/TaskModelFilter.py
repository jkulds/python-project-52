from django import forms
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter

from task_manager.models import LabelModel, TaskModel


class TaskModelFilter(FilterSet):
    labels = ModelChoiceFilter(
        queryset=LabelModel.objects.all(),
        label=_('Label')
    )

    own = BooleanFilter(
        label=_('own tasks'),
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
