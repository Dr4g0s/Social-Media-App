# Generated by Django 2.2.4 on 2019-08-25 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
