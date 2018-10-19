# Generated by Django 2.1.2 on 2018-10-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'flightstaff'), (2, 'security'), (3, 'admin')], default=3),
        ),
    ]
