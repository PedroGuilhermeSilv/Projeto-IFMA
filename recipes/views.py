from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Luiz Otávio',
    })

def recipe(request):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Luiz Otávio',
    })

def menu(request):
    return render(request, 'recipes/pages/menu.html', context={
        'name': 'Luiz Otávio',
    })
def cadastro(request):
    return render(request, 'recipes/pages/cadastro.html', context={
        'name': 'Luiz Otávio',
    })
