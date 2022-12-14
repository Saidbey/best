# Generated by Django 3.2.5 on 2022-10-24 12:02

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20221024_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='videoUrl',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
