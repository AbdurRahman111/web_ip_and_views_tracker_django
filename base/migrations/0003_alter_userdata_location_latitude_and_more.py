# Generated by Django 4.0.6 on 2022-07-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_userdata_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='location_latitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='location_longitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
