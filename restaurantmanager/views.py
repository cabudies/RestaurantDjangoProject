from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

# from restaurantmanager.Forms import AddNewMenu
from restaurantmanager.models import Menu


def index(request):
    template_name = loader.get_template('index.html')
    all_recipes = Menu.objects.all()
    # return HttpResponse("Hello World!")
    context = {
        "tag": "This text is from index.html page.",
        "menus": all_recipes
    }
    return HttpResponse(template_name.render(context, request))

def aboutus(request):
    # return HttpResponse("Thanks for websiting our website.")
    template_name = loader.get_template('aboutus.html')
    context = {
        'tag1': "Hello, welcome to about us page."
    }
    return HttpResponse(template_name.render(context, request))

def detail(request, recipe_name):
    template_name = loader.get_template('menuDetails.html')
    menu_details = Menu.objects.filter(recipe_name=recipe_name)
    context = {
        "details": menu_details
    }

    # return HttpResponse("Display the details of: %s " % recipe_name)
    return HttpResponse(template_name.render(context, request))

# def add_new_menu_item(request, menu_name):
#     if request.method == 'POST':
#         form = AddNewMenu(request.POST)
#
#         if form.is_valid():
#             pass
#     pass