from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    template_name = loader.get_template('index.html')
    # return HttpResponse("Hello World!")
    context = {
        "tag": "This text is from index.html page."
    }
    return HttpResponse(template_name.render(context, request))

def aboutus(request):
    # return HttpResponse("Thanks for websiting our website.")
    template_name = loader.get_template('aboutus.html')
    context = {
        'tag1': "Hello, welcome to about us page."
    }
    return HttpResponse(template_name.render(context, request))
