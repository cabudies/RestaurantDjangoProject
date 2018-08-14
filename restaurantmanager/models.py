from django.db import models

# Create your models here.
class Menu(models.Model):
    MENU_CATEGORY = (
        ('veg', 'Vegetarian'),
        ('non-veg', 'Non Vegetarian'),
    )

    recipe_name = models.CharField(max_length=50, help_text='Enter the menu item name',
                                   verbose_name='Menu Item name')

    menucategory = models.CharField(max_length=7, choices=MENU_CATEGORY, default='veg',
                                    help_text='Describe if the dish is veg or non-veg',
                                    verbose_name='Select the dish type')

    items_in_stock = models.IntegerField(default=0, help_text='Enter the number of items in stock',
                                         verbose_name='Number of items in stock')

    price = models.FloatField(default=0.0, help_text='Enter the price of the menu item',
                              verbose_name='Price of the menu item')

    def __str__(self):
        return self.recipe_name