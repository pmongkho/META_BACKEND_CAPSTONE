# Generated by Django 4.1.5 on 2023-01-26 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_booking_booking_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]