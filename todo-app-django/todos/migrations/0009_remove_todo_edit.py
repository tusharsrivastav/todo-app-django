# Generated by Django 2.2.2 on 2019-07-08 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_todo_edit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='edit',
        ),
    ]
