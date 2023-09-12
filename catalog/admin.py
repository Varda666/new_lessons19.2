from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'prod_name', 'prod_price', 'prod_cat')
    list_filter = ('prod_cat',)
    search_fields = ('prod_name', 'prod_desc',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name',)
