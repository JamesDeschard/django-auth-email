# Generated by Django 4.0.4 on 2022-04-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_first_connection',
            field=models.BooleanField(default=False),
        ),
    ]
