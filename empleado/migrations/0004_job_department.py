# Generated by Django 3.1.7 on 2021-03-26 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_auto_20210326_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='empleado.department', verbose_name='Puesto de Trabajo'),
        ),
    ]