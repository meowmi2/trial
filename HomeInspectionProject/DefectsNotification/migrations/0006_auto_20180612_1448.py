# Generated by Django 2.0.6 on 2018-06-12 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DefectsNotification', '0005_auto_20180612_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='block',
        ),
        migrations.RemoveField(
            model_name='address',
            name='level',
        ),
        migrations.RemoveField(
            model_name='address',
            name='unit',
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=128),
        ),
    ]
