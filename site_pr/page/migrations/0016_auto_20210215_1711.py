# Generated by Django 3.1.5 on 2021-02-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_auto_20210215_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
