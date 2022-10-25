# Generated by Django 3.2.5 on 2022-10-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='parters')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Partners',
            },
        ),
    ]