# Generated by Django 3.2 on 2021-05-08 01:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0024_remove_postcomment_usercomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='post_comment',
            field=models.ManyToManyField(blank=True, related_name='post_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]