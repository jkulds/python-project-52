from django import forms

from task_manager.models import TaskStatus


class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = TaskStatus
        fields = ['name']
