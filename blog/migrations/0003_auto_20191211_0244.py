# Generated by Django 2.1.7 on 2019-12-11 02:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191209_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claims',
            name='claim_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 2, 44, 55, 230901, tzinfo=utc)),
        ),
    ]
