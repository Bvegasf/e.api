# Generated by Django 3.1.7 on 2021-04-10 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0002_auto_20210409_0955'),
        ('empleado', '0007_auto_20210407_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='branch.branch'),
        ),
    ]