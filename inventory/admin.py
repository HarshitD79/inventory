from django.contrib import admin
from .views import (
    Category,
    Product,
    Supplier,
    StockIn,
    StockOut        
)
admin.site.register( Category)
admin.site.register( Product)
admin.site.register( Supplier)
admin.site.register( StockIn)
admin.site.register( StockOut)

# Register your models here.
