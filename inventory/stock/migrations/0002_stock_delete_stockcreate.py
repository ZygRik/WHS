# Generated by Django 4.0.3 on 2022-03-30 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name:')),
                ('oem_number', models.CharField(max_length=255, verbose_name='OEM#')),
                ('description', models.TextField(verbose_name='Description:')),
                ('product_url', models.URLField(verbose_name='Product URL:')),
                ('stocks_in_transit', models.PositiveSmallIntegerField(default=0, verbose_name='Number of stocks in transit')),
                ('min_qty_at_whs', models.PositiveSmallIntegerField(default=1, verbose_name='Min. quantity of stocks available:')),
                ('min_order_qty', models.PositiveSmallIntegerField(default=1, verbose_name='Min. order quantity:')),
            ],
        ),
        migrations.DeleteModel(
            name='StockCreate',
        ),
    ]
