from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    #permitecrear tupla (es algo que no puede cambiar) con los que mostramos
    list_display = ('id','name', 'description', 'price', 'stock', 'category')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
