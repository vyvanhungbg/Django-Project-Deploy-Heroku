# Generated by Django 3.2 on 2021-05-04 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20210504_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/images/user.png', null=True, upload_to='images'),
        ),
    ]