# Generated by Django 3.0.8 on 2021-06-23 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_auto_20210623_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/images/x.jpg', null=True, upload_to='images'),
        ),
    ]
