from django.contrib import admin

# Register your models here.
from restaurantmanager.models import Menu


class MenuDetailsAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'menucategory', 'price', 'items_in_stock')
    list_filter = ['price', 'menucategory']

admin.site.register(Menu, MenuDetailsAdmin)