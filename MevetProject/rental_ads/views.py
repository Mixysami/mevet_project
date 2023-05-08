from django.shortcuts import render
from .models import Rental, Category

def index(request):
    return render(request, 'index.html')

def kino(request):
    kino_category = Category.objects.get(name='kino')
    rental_list = Rental.objects.filter(category=kino_category)
    context = {"rental_list": rental_list}
    return render(request, 'kino.html', context)

def kon(request):
    return render(request, 'kon.html')

def pagefoto(request):
    return render(request, 'pagefoto.html')

def svadba(request):
    return render(request, 'svadba.html')

def banket(request):
    return render(request, 'banket.html')