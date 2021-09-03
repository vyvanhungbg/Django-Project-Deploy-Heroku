# Generated by Django 3.0.8 on 2021-05-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_alter_post_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='image_author',
            field=models.ImageField(blank=True, default='/images/x.jpg', null=True, upload_to='author'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='images',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, default='/images/x.jpg', null=True, upload_to='slides'),
        ),
        migrations.AlterField(
            model_name='music',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/images/x.jpg', null=True, upload_to='posts'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='images/user.jpg', upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
