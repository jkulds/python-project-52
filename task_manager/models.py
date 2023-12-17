from django.contrib.auth.models import User
from django.db import models

from base.TimeStampMixin import TimeStampMixin


class TaskStatus(TimeStampMixin):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class TaskModel(TimeStampMixin):
    title = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(max_length=4096, blank=True)
    assignee = models.ForeignKey(User, on_delete=models.PROTECT,)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT,
                               related_name='statuses')
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name='authored_tasks')

    def __str__(self):
        return self.title


