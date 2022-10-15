# Generated by Django 4.1.2 on 2022-10-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='title',
        ),
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(choices=[('Kyrgyzstan', 'Kyrgyzstan'), ('Kazakhstan', 'Kazakhstan'), ('Uzbekistan', 'Uzbekistan'), ('Tajikistan', 'Tajikistan')], max_length=255),
        ),
    ]
