# Generated by Django 2.2.10 on 2021-04-14 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_todolist_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='owner',
            new_name='manage',
        ),
    ]
