from django.urls import path

from . import views

# recipes:recipe - para não usar recipes-recipe, recipes-home, etc)
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:categoria_id>/',
         views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
