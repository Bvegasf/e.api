# Generated by Django 3.1.6 on 2021-03-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210310_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(max_length=50, verbose_name='Descripcion del producto'),
        ),
    ]
