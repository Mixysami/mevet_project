from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import Rental, Category, RentalImage
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from .forms import RentalForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid credentials')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def kino(request):
    kino_category = Category.objects.get(name='kino')
    rental_list = Rental.objects.filter(category=kino_category)
    context = {"rental_list": rental_list}
    return render(request, 'kino.html', context)


def kon(request):
    kon_category = Category.objects.get(name='kon')
    rental_list = Rental.objects.filter(category=kon_category)
    context = {"rental_list": rental_list}
    return render(request, 'kon.html', context)


def pagefoto(request):
    pagefoto_category = Category.objects.get(name='pagefoto')
    rental_list = Rental.objects.filter(category=pagefoto_category)
    context = {"rental_list": rental_list}
    return render(request, 'pagefoto.html', context)


def svadba(request):
    svadba_category = Category.objects.get(name='svadba')
    rental_list = Rental.objects.filter(category=svadba_category)
    context = {"rental_list": rental_list}
    return render(request, 'svadba.html', context)


def banket(request):
    banket_category = Category.objects.get(name='banket')
    rental_list = Rental.objects.filter(category=banket_category)
    context = {"rental_list": rental_list}
    return render(request, 'banket.html', context)



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




def favorites(request):
    rental_list = Rental.objects.filter(id__in=request.session.get('favorites', []))
    context = {'rental_list': rental_list}
    return render(request, 'favorites.html', context)


def add_rental(request):
    if request.method == 'POST':
        form = RentalForm(request.POST, request.FILES)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.user = request.user  # Связываем объявление с пользователем
            form.save()
            return redirect('rental_manage')
    else:
        form = RentalForm()
    return render(request, 'add_rental.html', {'form': form})

@login_required
def rental_manage(request):
    user = request.user
    rental_list = Rental.objects.filter(user=request.user)
    return render(request, 'rental_manage.html', {'rental_list': rental_list})







