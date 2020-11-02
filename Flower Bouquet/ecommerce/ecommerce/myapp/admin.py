from django.contrib import admin
from .models import *
from django.contrib.admin.options import ModelAdmin

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'address_line_2',
        'city',
        'zip_code',
        'address_type',
    ]


admin.site.register(Category)
admin.site.register(Address, AddressAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','price')
    list_filter = ("title",)
    search_fields = ['title', 'price']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Product, ProductAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(SizeVariation)
admin.site.register(ColourVariation)


