# Generated by Django 3.2.5 on 2022-10-27 22:26

import apps.shared.utils.valid_size
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20221024_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='blog/comment', validators=[apps.shared.utils.valid_size.validate_img_size]),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='blog/news'),
        ),
        migrations.AlterField(
            model_name='news',
            name='video',
            field=models.FileField(blank=True, upload_to='blog/news'),
        ),
    ]