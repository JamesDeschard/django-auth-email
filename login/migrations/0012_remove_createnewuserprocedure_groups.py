# Generated by Django 4.0.4 on 2022-04-26 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_remove_createnewuserprocedure_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createnewuserprocedure',
            name='groups',
        ),
    ]