# Generated by Django 3.0.5 on 2022-04-23 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_bookingandpurchaseshistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingandpurchaseshistory',
            name='made_on',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
