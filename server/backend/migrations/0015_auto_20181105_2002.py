# Generated by Django 2.1.2 on 2018-11-06 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_riderequests_isaccepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riderequests',
            name='driverLatitude',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='riderequests',
            name='driverLongitude',
            field=models.FloatField(default=0, null=True),
        ),
    ]
