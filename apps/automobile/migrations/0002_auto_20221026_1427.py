# Generated by Django 3.2.5 on 2022-10-26 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automobile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='about',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='title',
            new_name='model',
        ),
        migrations.RemoveField(
            model_name='positioncategory',
            name='mileage',
        ),
        migrations.RemoveField(
            model_name='positioncategory',
            name='name',
        ),
        migrations.AddField(
            model_name='car',
            name='carbody',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Usedcars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('year', models.IntegerField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default=2022, verbose_name='year')),
                ('cost', models.FloatField()),
                ('engine', models.CharField(max_length=255)),
                ('transmission_box', models.CharField(max_length=255)),
                ('drive_type', models.CharField(max_length=255)),
                ('mileage', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automobile.car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
