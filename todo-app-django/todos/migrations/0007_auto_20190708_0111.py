# Generated by Django 2.2.2 on 2019-07-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_auto_20190708_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
