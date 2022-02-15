from django.http import Http404
from django.shortcuts import render
from utils.recipes.factory import make_recipe

# ou desse jeito  from .models import Recipe
from recipes.models import Recipe

# Create your views here.


def home(request):
    receitas = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': receitas,
        #        'recipes': [make_recipe() for _ in range(10)],
    })


def category(request, categoria_id):
    receitas = Recipe.objects.filter(
        category__id=categoria_id,
        is_published=True
    ).order_by('-id')

    if not receitas:
        raise Http404('Not Found')

    return render(request, 'recipes/pages/category.html', context={
        'recipes': receitas,
        'title': f'{receitas.first().category.name} - Category | '
        #        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
