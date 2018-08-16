from django import forms

class AddNewMenu(forms.Form):
    MENU_CATEGORY = (
        ('veg', 'Vegetarian'),
        ('non-veg', 'Non Vegetarian'),
    )

    recipe_name = forms.CharField(max_length=50, help_text='Enter the menu item name',
                                   verbose_name='Menu Item name')

    menucategory = forms.CharField(max_length=7, choices=MENU_CATEGORY, default='veg',
                                    help_text='Describe if the dish is veg or non-veg',
                                    verbose_name='Select the dish type')

    items_in_stock = forms.IntegerField(default=0, help_text='Enter the number of items in stock',
                                         verbose_name='Number of items in stock')

    price = forms.FloatField(default=0.0, help_text='Enter the price of the menu item',
                              verbose_name='Price of the menu item')


class AddName(forms.Form):
    name = forms.CharField(min_length=3, help_text='Enter the name',
                                  verbose_name='Name: ')