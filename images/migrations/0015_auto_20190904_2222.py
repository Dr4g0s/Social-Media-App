# Generated by Django 2.2.4 on 2019-09-04 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0014_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='total_comments',
        ),
        migrations.RemoveField(
            model_name='image',
            name='users_comment',
        ),
    ]
