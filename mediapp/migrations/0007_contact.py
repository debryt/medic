# Generated by Django 5.1.6 on 2025-02-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0006_rename_phone_number_appointment_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
