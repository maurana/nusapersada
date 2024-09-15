import django.db.models.deletion
from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    initial = False

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customers_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='CUSTOMERS_ID')),
                ('customers_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-customers_id'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('products_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='PRODUCTS_ID')),
                ('products_name', models.CharField(max_length=250)),
                ('products_code', models.CharField(max_length=15)),
                ('products_price', models.FloatField(blank=True, null=True)),
                ('products_stock', models.IntegerField(db_default=0)),
                ('products_status', models.CharField(db_default='0', max_length=11)),
            ],
            options={
                'ordering': ['-products_id'],
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('sales_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='SALES_ID')),
                ('sales_code', models.CharField(max_length=15)),
                ('sales_date', models.DateField(blank=True, null=True)),
                ('sale_items_total', models.IntegerField(db_default=0)),
                ('sale_price_total', models.FloatField(blank=True, null=True)),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='v1.customers')),
            ],
            options={
                'ordering': ['-sales_id'],
            },
        ),
        migrations.CreateModel(
            name='Sale_Items',
            fields=[
                ('item_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ITEM_ID')),
                ('item_price', models.FloatField(blank=True, null=True)),
                ('item_qty', models.IntegerField(db_default=0)),
                ('is_verify', models.IntegerField(db_default=0)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='v1.products')),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='v1.sales')),
            ],
            options={
                'ordering': ['-item_id'],
            },
        ),
    ]
