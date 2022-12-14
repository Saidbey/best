# Generated by Django 3.2.5 on 2022-10-23 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('automobile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cridet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('month', models.IntegerField(default=12)),
                ('status', models.IntegerField(choices=[(1, 'Credit'), (2, 'Leasing')])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cridets', to='automobile.car')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cridets', to='automobile.positioncategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=1)),
                ('sum', models.DecimalField(decimal_places=3, default=0, max_digits=15)),
                ('percent', models.FloatField(default=12)),
                ('per_month', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('credit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='calculator.cridet')),
            ],
        ),
    ]
