# Generated by Django 3.1.7 on 2021-03-26 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='fecha de creacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='delete_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de eliminacion'),
        ),
        migrations.AddField(
            model_name='department',
            name='modified_date',
            field=models.DateField(auto_now=True, verbose_name='fecha de modificacion'),
        ),
        migrations.AddField(
            model_name='department',
            name='state',
            field=models.BooleanField(default=True, verbose_name='estado'),
        ),
        migrations.AddField(
            model_name='job',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='fecha de creacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='delete_date',
            field=models.DateField(auto_now=True, verbose_name='Fecha de eliminacion'),
        ),
        migrations.AddField(
            model_name='job',
            name='modified_date',
            field=models.DateField(auto_now=True, verbose_name='fecha de modificacion'),
        ),
        migrations.AddField(
            model_name='job',
            name='state',
            field=models.BooleanField(default=True, verbose_name='estado'),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
