# Generated by Django 2.2.4 on 2019-09-04 16:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0010_auto_20190903_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='total_comments',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='users_comment',
            field=models.ManyToManyField(blank=True, related_name='images_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
