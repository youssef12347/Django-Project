# Generated by Django 3.2.13 on 2022-04-20 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultation', '0003_consultation_startdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultation',
            old_name='startdate',
            new_name='date',
        ),
    ]
