# Generated by Django 4.2.7 on 2023-12-17 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_labelmodel_taskmodel_labels'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLabelRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task_manager.labelmodel')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager.taskmodel')),
            ],
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', through='task_manager.TaskLabelRelation', to='task_manager.labelmodel'),
        ),
    ]
