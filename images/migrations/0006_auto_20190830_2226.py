# Generated by Django 2.2.4 on 2019-08-30 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_auto_20190830_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(default='test title', max_length=200),
        ),
    ]
