# Generated by Django 2.2.11 on 2020-03-15 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_Done',
            field=models.BooleanField(default=False),
        ),
    ]