from django.contrib import admin
from .models import Company , Product , Supplier,MedOrder_interm
# Register your models here.
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(MedOrder_interm)