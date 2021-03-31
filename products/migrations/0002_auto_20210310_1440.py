# Generated by Django 3.1.6 on 2021-03-10 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryproduct',
            name='measure_unit',
        ),
        migrations.AddField(
            model_name='products',
            name='category_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='Categoria de Producto'),
        ),
        migrations.AddField(
            model_name='products',
            name='measure_unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de medida'),
        ),
    ]
