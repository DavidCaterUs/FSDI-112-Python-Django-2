from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre


# Create your views here.
def index(request):
    # read data from db
    genres = Genre.objects.all()

    """
    get all: Class.objects.all()
    id:Class.objcts.get(id=1)

    filter:
    """

    # send data and render

    return render(request, 'views/index.html', {'title': 'Index Page', 'items': genres})


def catalog (request):
    return render (request, 'views/catalog.html') 

def welcome(request):
    return render(request, 'views/welcome.html', {'title': 'Welcome', 'rows': 2})

def myname(request):
    return HttpResponse("Hello my name is Kleibert! :D ")
