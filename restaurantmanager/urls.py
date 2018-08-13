from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('aboutus', views.aboutus)
]