# Generated by Django 5.0.6 on 2024-09-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='typex',
            field=models.CharField(choices=[('urgent', 'Urgent'), ('epic', 'Epic'), ('normal', 'Normal'), ('low', 'Low Priority')], default='normal', max_length=20),
        ),
    ]
