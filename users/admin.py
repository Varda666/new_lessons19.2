from django.contrib import admin

from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'phone', 'country', 'img')
    list_filter = ('email', 'password', 'phone', 'country', 'img')
    search_fields = ('email', 'password', 'phone', 'country', 'img')





