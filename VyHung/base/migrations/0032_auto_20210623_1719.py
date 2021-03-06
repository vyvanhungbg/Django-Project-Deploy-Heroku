# Generated by Django 3.0.8 on 2021-06-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_auto_20210527_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='image_author',
            field=models.ImageField(default='images/x.jpg', upload_to='author'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, default='images/x.jpg', null=True, upload_to='slides'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='images/x.jpg', null=True, upload_to='posts'),
        ),
    ]
