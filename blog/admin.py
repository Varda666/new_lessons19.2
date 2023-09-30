from django.contrib import admin

from blog.models import BlogMaterial


# Register your models here.
@admin.register(BlogMaterial)
class BlogMaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'content')
    list_filter = ('name', 'content')
    search_fields = ('name', 'content', 'created_at', 'views_count', 'published')
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
