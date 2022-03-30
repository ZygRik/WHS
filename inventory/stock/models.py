from django.db import models
from stock.UOM import UOM


# Basic information about stock to enter
class Stock(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name:")
    UoM = models.CharField(max_length=250, choices=UOM)
    oem_number = models.CharField(max_length=255, verbose_name="OEM#")
    description = models.TextField(verbose_name="Description:")
    product_url = models.URLField(verbose_name="Product URL:")
    stocks_in_transit = models.PositiveSmallIntegerField(default=0, verbose_name="Number of stocks in transit")
    min_qty_at_whs = models.PositiveSmallIntegerField(default=1, verbose_name="Min. quantity of stocks available:")
    min_order_qty = models.PositiveSmallIntegerField(default=1, verbose_name="Min. order quantity:")
    stock_entry_date = models.DateField(verbose_name="Stock created at:", editable=False, auto_now_add=True)
    
    def __str__(self):
        return f'Stock#:{self.id} | Name: "{self.name}": | date stock created:{self.stock_entry_date}'

