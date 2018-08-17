from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Index path
    path('', views.index),
    # About us page, url - index/aboutus
    path('aboutus', views.aboutus),
    # Load only specific menu item
    # path('<slug:recipe_name>', views.detail, name='detail'),
    # Add new Menu
    path('addNewMenu', views.add_new_name, name='add-new-name'),
    # Custom Login Template
    path('login/', views.custom_login_view, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view())
]