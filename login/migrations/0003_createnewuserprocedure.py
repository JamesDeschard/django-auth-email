# Generated by Django 4.0.4 on 2022-04-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_user_is_first_connection'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateNewUserProcedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=128)),
            ],
        ),
    ]
