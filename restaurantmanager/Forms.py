from django import forms

# class AddNewMenu(forms.Form):
#     recipe_name = forms.CharField(max_length=50)
#     menu_category = forms.CharField(max_length=7)
#     items_in_stock = forms.IntegerField(default=0)
#     price = forms.FloatField(default=0.0)
#
#     def clean(self):
#         cleaned_data = super(AddNewMenu, self).clean()
#         recipe_name = cleaned_data.get('recipe_name')
#         menu_category = cleaned_data.get('menu_category')
#         items_in_stock = cleaned_data.get('items_in_stock')
#         price = cleaned_data.get('price')
#
#         if not recipe_name and not menu_category and not items_in_stock and not price:
#             raise forms.ValidationError('Enter all the values correctly.')


class AddName(forms.Form):
    name = forms.CharField()