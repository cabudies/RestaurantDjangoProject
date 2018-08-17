from django.contrib import admin

# Register your models here.
from restaurantmanager.models import Menu, Name


class MenuDetailsAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'menucategory', 'price', 'items_in_stock')
    list_filter = ['price', 'menucategory']

class NameDetailsAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Menu, MenuDetailsAdmin)
admin.site.register(Name, NameDetailsAdmin)