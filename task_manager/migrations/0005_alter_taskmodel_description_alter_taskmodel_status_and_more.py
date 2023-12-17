# Generated by Django 4.2.7 on 2023-12-17 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0004_alter_taskmodel_assignee_alter_taskmodel_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='description',
            field=models.TextField(blank=True, max_length=4096),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='statuses', to='task_manager.taskstatus'),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
