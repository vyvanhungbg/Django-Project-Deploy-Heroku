# Generated by Django 3.2 on 2021-05-01 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_images_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='favorites',
            field=models.ManyToManyField(to='base.favorite'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='images_slide',
            field=models.ManyToManyField(to='base.images'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='songs',
            field=models.ManyToManyField(to='base.song'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='base.Tag'),
        ),
    ]