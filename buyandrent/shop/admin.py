from django.contrib import admin
from .models import Category, House

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class HouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(House, HouseAdmin)
