# Generated by Django 2.1.7 on 2019-12-11 17:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191211_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claims',
            name='claim_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 17, 25, 5, 136081, tzinfo=utc)),
        ),
    ]
