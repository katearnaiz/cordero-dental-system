from django.contrib import admin
from .models import Supplier
from .models import Customer
# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display=['contact_number','business_name','contact_person','address1','address2','special_notes']

class CustomerAdmin(admin.ModelAdmin):
    list_display=['customer_name','contact_number']

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Customer, CustomerAdmin)
