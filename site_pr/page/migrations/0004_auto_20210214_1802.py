# Generated by Django 3.1.5 on 2021-02-14 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
