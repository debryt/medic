# Generated by Django 5.1.6 on 2025-02-27 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('qualification', models.CharField(max_length=100)),
            ],
        ),
    ]
