# Generated by Django 2.1.2 on 2018-10-06 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20181004_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='ccIsDefault',
            field=models.BooleanField(default=False),
        ),
    ]