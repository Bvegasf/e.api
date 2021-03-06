# Generated by Django 3.1.7 on 2021-04-07 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ECHO', 'Echomert'), ('HIPER', 'Hipermerch'), ('MEGA', 'Mega')], default='ECHO', max_length=200, verbose_name='nombre')),
                ('adress', models.TextField(blank=True, max_length=400)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.city')),
                ('continental_region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.continentalregion')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='location.country')),
            ],
        ),
    ]
