from django import forms
from django.utils.translation import gettext as _

from task_manager.models import LabelModel


class LabelForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150, required=True, label=_("label name")
    )

    class Meta:
        model = LabelModel
        fields = ['name']
        