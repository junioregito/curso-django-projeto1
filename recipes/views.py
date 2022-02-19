from django.shortcuts import get_list_or_404, get_object_or_404, render
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
    receitas = get_list_or_404(
        Recipe.objects.filter(
            category__id=categoria_id,
            is_published=True
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': receitas,
        'title': f'{receitas[0].category.name} - Category | '
    })


def recipe(request, id):
    receita = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': receita,
        'is_detail_page': True,
    })
