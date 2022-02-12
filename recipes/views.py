from django.shortcuts import render


# Create your views here.
def home(requeste):
    return render(requeste, 'recipes/pages/home.html', context={
        'name': 'Junior Egito',
    })
