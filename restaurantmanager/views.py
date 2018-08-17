from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
from django.template import loader

# from restaurantmanager.Forms import AddNewMenu
from restaurantmanager.Forms import AddName
from restaurantmanager.models import Menu, Name


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

# @login_required(login_url='/accounts/login/')
def add_new_name(request):
    # if request.user.is_authenticated:
    #     username = request.user.username
    #     print("User is logged in. Logged in user's name is: ", username)

    if request.method == 'POST':
        form = AddName(request.POST)

        if form.is_valid():
            name = request.POST.get('name')
            new_entry = Name(name = name)
            new_entry.save()

    return render(request, 'addNewMenu.html')
    # return HttpResponse(template_name.render(request, form = form))

def custom_login_view(request):
    name = request.POST.get('username')
    pwd = request.POST.get('password')
    user = authenticate(username = name, password = pwd)
    global context
    if user is not None:
        login(request, user)
        context = {
            'success': 'User logged in'
        }
        return HttpResponse("User logged in successfully." + name)
    else:
        context = {
            'success' : 'Invalid credentials'
        }

    return HttpResponse("Sorry invalid credentials.")

# @login_required(login_url='/accounts/login/')
# def add_new_menu(request):
#     # if request.user.is_authenticated:
#     #     username = request.user.username
#     #     print("User is logged in. Logged in user's name is: ", username)
#
#     if request.method == 'POST':
#         form = AddNewMenu(request.POST)
#
#         if form.is_valid() and request.user.is_authenticated:
#             name = request.POST.get('name')
#             new_entry = Name(name = name)
#             new_entry.save()
#
#     return render(request, 'addNewMenu.html')