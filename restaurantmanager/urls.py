from django.urls import path

from . import views

urlpatterns = [
    # Index path
    path('', views.index),
    # About us page, url - index/aboutus
    path('aboutus', views.aboutus),
    # Load only specific menu item
    path('<slug:recipe_name>', views.detail, name='detail'),
    # Add new Menu
    # path('addNewMenu', views.add_new_menu_item, name='add-new-menu')
]