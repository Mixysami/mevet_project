from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Rental, Category, RentalImage

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

def rental_detail(request, category_name, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    images = rental.images.all()
    context = {'rental': rental, 'images': images}
    return render(request, 'rental_detail.html', context)

def rental_search(request):
    query = request.GET.get('query', '')

    rental_list = Rental.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )

    context = {'rental_list': rental_list}
    return render(request, 'rental_search_results.html', context)


