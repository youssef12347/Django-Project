# Generated by Django 3.0.5 on 2022-04-27 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0023_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]
