# Generated by Django 4.0.4 on 2022-04-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_remove_createnewuserprocedure_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='createnewuserprocedure',
            name='groups',
            field=models.CharField(choices=[('test_permissions', 'test_permissions'), ('test_2', 'test_2')], default='', max_length=128, unique=True),
            preserve_default=False,
        ),
    ]
