# Generated by Django 3.1.5 on 2021-03-06 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 6, 8, 4, 32, 674212, tzinfo=utc)),
        ),
    ]