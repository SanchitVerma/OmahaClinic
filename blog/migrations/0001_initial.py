# Generated by Django 2.0.5 on 2019-11-06 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('appointment_number', models.IntegerField(primary_key=True, serialize=False)),
                ('appointment_date', models.DateField()),
                ('appointment_time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
        migrations.CreateModel(
            name='Claims',
            fields=[
                ('claim_number', models.IntegerField(primary_key=True, serialize=False)),
                ('claim_date', models.DateTimeField()),
                ('claim_amount', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Claim',
                'verbose_name_plural': 'Claims',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('cust_name', models.CharField(max_length=50)),
                ('insurance_number', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('dob', models.DateTimeField()),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Providers',
            fields=[
                ('provider_name', models.CharField(max_length=50)),
                ('provider_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('speciality', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Provider',
                'verbose_name_plural': 'Providers',
            },
        ),
        migrations.AddField(
            model_name='claims',
            name='insurance_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='d', to='blog.Customers'),
        ),
        migrations.AddField(
            model_name='claims',
            name='provider_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b', to='blog.Providers'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='insurance_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='b', to='blog.Customers'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='provider_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a', to='blog.Providers'),
        ),
    ]
