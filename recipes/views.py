#from utils.recipes.factory import make_recipe
#from django.core.paginator import Paginator
import os


from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.pagination import make_pagination

# ou desse jeito  from .models import Recipe
from recipes.models import Recipe

# ou somente os pacotesfrom django.contrib.messages import success, error, debug
# nessa caso serira


# Create your views here.

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


def home(request):
    receitas = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, receitas, PER_PAGE)

    return render(request, 'recipes/pages/home.html', context={
        #        'recipes': receitas,
        'recipes': page_obj,
        'pagination_range': pagination_range

        #        'recipes': [make_recipe() for _ in range(10)],
    })


def category(request, categoria_id):
    receitas = get_list_or_404(
        Recipe.objects.filter(
            category__id=categoria_id,
            is_published=True
        ).order_by('-id')
    )

    page_obj, pagination_range = make_pagination(request, receitas, PER_PAGE)

    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'title': f'{receitas[0].category.name} - Category | '
    })


def recipe(request, id):
    receita = get_object_or_404(Recipe, pk=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': receita,
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)

    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })
