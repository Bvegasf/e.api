# Generated by Django 3.1.6 on 2021-03-09 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='fecha de modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('name', models.CharField(max_length=20, verbose_name='nombre')),
                ('description', models.CharField(max_length=50, verbose_name='descripcion')),
            ],
            options={
                'verbose_name': 'Categoria de Producto',
                'verbose_name_plural': 'Categorias de Productos',
            },
        ),
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='fecha de modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('description', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Unidad de Medida',
                'verbose_name_plural': 'Unidades de Medidas',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='fecha de modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre de Producto')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Descripcion dle producto')),
                ('image_product', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
            options={
                'verbose_name': 'Productos',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='fecha de modificacion')),
                ('delete_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminacion')),
                ('descuent_value', models.PositiveIntegerField(default=0)),
                ('category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct', verbose_name='indicador de oferta')),
            ],
            options={
                'verbose_name': 'Indicador de descuento',
                'verbose_name_plural': 'Indicadores de descuentos',
            },
        ),
        migrations.CreateModel(
            name='HistoricalMeasureUnit',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='fecha de creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='fecha de modificacion')),
                ('delete_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de eliminacion')),
                ('description', models.CharField(db_index=True, max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Unidad de Medida',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='measure_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.measureunit', verbose_name='Unidad de medida'),
        ),
    ]
