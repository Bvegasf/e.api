# Generated by Django 3.1.7 on 2021-04-06 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContinentalRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=230, unique=True, verbose_name='nombre')),
                ('name_corto', models.CharField(max_length=5, verbose_name='nombre corto')),
            ],
            options={
                'verbose_name': 'Region Continental',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=230, unique=True, verbose_name='nombre')),
                ('code', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='codigo')),
                ('continental_region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.continentalregion')),
            ],
            options={
                'verbose_name': 'Pais',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=230, verbose_name='nombre')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.country')),
            ],
            options={
                'verbose_name': 'Ciudad',
            },
        ),
    ]