# Generated by Django 3.2.5 on 2022-10-23 08:46

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('cost_from', models.DecimalField(decimal_places=3, max_digits=9, null=True)),
                ('color', colorfield.fields.ColorField(choices=[('#FFFFFF', 'white'), ('#000000', 'black'), ('#FF0000', 'red')], default='#FFFFFF', image_field=None, max_length=18, samples=None)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('Oilaviy', 'Family'), ('Sports', 'Sports'), ('Sayohat', 'Journey')], max_length=100, null=True)),
                ('internal_possibility', models.TextField()),
                ('appearance', models.TextField()),
                ('internal_photo', models.ImageField(upload_to='indernal_pics')),
                ('external_photo', models.ImageField(upload_to='external_pics')),
                ('side_photo', models.ImageField(upload_to='side_pics')),
                ('discount', models.IntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CarCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('logo', models.ImageField(upload_to='company_logo')),
                ('about', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('bonus', models.CharField(max_length=100, null=True)),
                ('details', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Bonus',
            },
        ),
        migrations.CreateModel(
            name='PositionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('year', models.IntegerField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default=2022, verbose_name='year')),
                ('cost', models.FloatField()),
                ('engine', models.CharField(max_length=255)),
                ('engine_size', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('available_volume', models.CharField(max_length=255)),
                ('drive_type', models.CharField(max_length=255)),
                ('transmission_box', models.CharField(max_length=255)),
                ('overclocking_time', models.FloatField()),
                ('max_speed', models.IntegerField()),
                ('mileage', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('lockingRearWheelDifferential', models.BooleanField(default=False)),
                ('automaticAutoHold', models.BooleanField(default=False)),
                ('childSeatLock', models.BooleanField(default=False)),
                ('front_breakes', models.CharField(max_length=100, null=True)),
                ('rear_breakes', models.CharField(max_length=100, null=True)),
                ('front_wheels', models.SlugField(max_length=100, null=True)),
                ('rear_wheels', models.SlugField(max_length=100, null=True)),
                ('led_headlight', models.CharField(max_length=255)),
                ('full_weight', models.FloatField()),
                ('empty_weight', models.FloatField()),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('length', models.FloatField()),
                ('seats_count', models.IntegerField()),
                ('rearSuspension', models.CharField(max_length=100, null=True)),
                ('brakeAssistSystem', models.CharField(max_length=100, null=True)),
                ('antilockBrakingSystem', models.CharField(max_length=100, null=True)),
                ('hillsStartAssist', models.CharField(max_length=100, null=True)),
                ('PassengerAirbagWithDeactivationFunction', models.BooleanField(default=False)),
                ('FrontPassengerAirbag', models.BooleanField(default=False)),
                ('AdditionalBrakeLight', models.BooleanField(default=False)),
                ('eraGlonass', models.BooleanField(default=False)),
                ('isofixMount', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automobile.car')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='car',
            name='bonusForCustomers',
            field=models.ManyToManyField(related_name='gifts', to='automobile.Gifts'),
        ),
        migrations.AddField(
            model_name='car',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='automobile.carcompany'),
        ),
    ]
