from django.contrib import admin

from .models import Category, Recipe

# Register your models here.

# @admin.register

# tem essa maneira


class CategoryAdmin(admin.ModelAdmin):
    ...


# tem essa outra_maneira.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
