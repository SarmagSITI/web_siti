from django.shortcuts import render
from .models import HomePage, AboutPage

def index(request):
    home_page = HomePage.load()
    context={'home_page' : home_page,}
    return render(request, 'staticpage/index.html', context)

def about(request):
    about_page = AboutPage.load()
    context={'about_page' : about_page,}
    return render(request, 'staticpage/about.html', context)
