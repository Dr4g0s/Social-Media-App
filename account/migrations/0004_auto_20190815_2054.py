# Generated by Django 2.2.4 on 2019-08-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190815_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
