# Generated by Django 4.1.5 on 2023-01-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='table_no',
            field=models.IntegerField(default=0),
        ),
    ]
