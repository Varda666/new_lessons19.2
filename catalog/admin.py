from django.contrib import admin

from catalog.models import Product, Category, Contact


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'cat')
    list_filter = ('cat',)
    search_fields = ('name', 'desc',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'message',)

