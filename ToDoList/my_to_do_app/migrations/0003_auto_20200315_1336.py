# Generated by Django 2.2.11 on 2020-03-15 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_app', '0002_todo_is_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='is_Done',
            new_name='isDone',
        ),
    ]
