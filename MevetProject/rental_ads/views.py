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
from django.conf import settings
from django.forms import inlineformset_factory
from django.contrib import messages
from .models import Favorite

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

    # Получение значения выбранного фильтра
    filter_value = request.GET.get('filter')

    # Фильтрация списка объявлений в соответствии с выбранным фильтром
    if filter_value == 'r1':
        rental_list = rental_list.order_by('-created_at')  # По новизне
    elif filter_value == 'r2':
        rental_list = rental_list.order_by('-views_count')  # По популярности
    elif filter_value == 'r3':
        rental_list = rental_list.order_by('price')  # По цене по возрастанию
    elif filter_value == 'r4':
        rental_list = rental_list.order_by('-price')  # По цене по убыванию

    # Обновление количества просмотров объявлений
    for rental in rental_list:
        rental.views_count += 1
        rental.save()

    # Добавление выбранного значения фильтра в контекст
    context = {
        "rental_list": rental_list,
        "selected_filter": filter_value  # Передача выбранного значения фильтра в шаблон
    }
    return render(request, 'kino.html', context)


def kon(request):
    kon_category = Category.objects.get(name='kon')
    rental_list = Rental.objects.filter(category=kon_category)

    # Получение значения выбранного фильтра
    filter_value = request.GET.get('filter')

    # Фильтрация списка объявлений в соответствии с выбранным фильтром
    if filter_value == 'r1':
        rental_list = rental_list.order_by('-created_at')  # По новизне
    elif filter_value == 'r2':
        rental_list = rental_list.order_by('-views_count')  # По популярности
    elif filter_value == 'r3':
        rental_list = rental_list.order_by('price')  # По цене по возрастанию
    elif filter_value == 'r4':
        rental_list = rental_list.order_by('-price')  # По цене по убыванию

    # Обновление количества просмотров объявлений
    for rental in rental_list:
        rental.views_count += 1
        rental.save()

    # Добавление выбранного значения фильтра в контекст
    context = {
        "rental_list": rental_list,
        "selected_filter": filter_value  # Передача выбранного значения фильтра в шаблон
    }
    return render(request, 'kon.html', context)


def pagefoto(request):
    pagefoto_category = Category.objects.get(name='pagefoto')
    rental_list = Rental.objects.filter(category=pagefoto_category)

    # Получение значения выбранного фильтра
    filter_value = request.GET.get('filter')

    # Фильтрация списка объявлений в соответствии с выбранным фильтром
    if filter_value == 'r1':
        rental_list = rental_list.order_by('-created_at')  # По новизне
    elif filter_value == 'r2':
        rental_list = rental_list.order_by('-views_count')  # По популярности
    elif filter_value == 'r3':
        rental_list = rental_list.order_by('price')  # По цене по возрастанию
    elif filter_value == 'r4':
        rental_list = rental_list.order_by('-price')  # По цене по убыванию

    # Обновление количества просмотров объявлений
    for rental in rental_list:
        rental.views_count += 1
        rental.save()

    # Добавление выбранного значения фильтра в контекст
    context = {
        "rental_list": rental_list,
        "selected_filter": filter_value  # Передача выбранного значения фильтра в шаблон
    }
    return render(request, 'pagefoto.html', context)


def svadba(request):
    svadba_category = Category.objects.get(name='svadba')
    rental_list = Rental.objects.filter(category=svadba_category)

    # Получение значения выбранного фильтра
    filter_value = request.GET.get('filter')

    # Фильтрация списка объявлений в соответствии с выбранным фильтром
    if filter_value == 'r1':
        rental_list = rental_list.order_by('-created_at')  # По новизне
    elif filter_value == 'r2':
        rental_list = rental_list.order_by('-views_count')  # По популярности
    elif filter_value == 'r3':
        rental_list = rental_list.order_by('price')  # По цене по возрастанию
    elif filter_value == 'r4':
        rental_list = rental_list.order_by('-price')  # По цене по убыванию

    # Обновление количества просмотров объявлений
    for rental in rental_list:
        rental.views_count += 1
        rental.save()

    # Добавление выбранного значения фильтра в контекст
    context = {
        "rental_list": rental_list,
        "selected_filter": filter_value  # Передача выбранного значения фильтра в шаблон
    }
    return render(request, 'svadba.html', context)


def banket(request):
    banket_category = Category.objects.get(name='banket')
    rental_list = Rental.objects.filter(category=banket_category)

    # Получение значения выбранного фильтра
    filter_value = request.GET.get('filter')

    # Фильтрация списка объявлений в соответствии с выбранным фильтром
    if filter_value == 'r1':
        rental_list = rental_list.order_by('-created_at')  # По новизне
    elif filter_value == 'r2':
        rental_list = rental_list.order_by('-views_count')  # По популярности
    elif filter_value == 'r3':
        rental_list = rental_list.order_by('price')  # По цене по возрастанию
    elif filter_value == 'r4':
        rental_list = rental_list.order_by('-price')  # По цене по убыванию

    # Обновление количества просмотров объявлений
    for rental in rental_list:
        rental.views_count += 1
        rental.save()

    # Добавление выбранного значения фильтра в контекст
    context = {
        "rental_list": rental_list,
        "selected_filter": filter_value  # Передача выбранного значения фильтра в шаблон
    }
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


def add_rental(request):
    if request.method == 'POST':
        form = RentalForm(request.POST, request.FILES)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.user = request.user  # Связываем объявление с пользователем
            form.save()

            # Обработка загрузки дополнительных фотографий
            images = request.FILES.getlist('images')
            for image in images:
                RentalImage.objects.create(rental=rental, image=image)

            return redirect('rental_manage')
    else:
        form = RentalForm()
    return render(request, 'add_rental.html', {'form': form})

@login_required
def rental_manage(request):
    user = request.user
    rental_list = Rental.objects.filter(user=user)
    username = user.username  # Получение имени пользователя
    return render(request, 'rental_manage.html', {'rental_list': rental_list, 'username': username})

@login_required
def delete_rental(request, rental_id):
    rental = get_object_or_404(Rental, pk=rental_id, user=request.user)
    rental.delete()
    return redirect('rental_manage')

@login_required
def edit_rental(request, rental_id):
    rental = get_object_or_404(Rental, pk=rental_id, user=request.user)

    if request.method == 'POST':
        form = RentalForm(request.POST, request.FILES, instance=rental)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.user = request.user
            rental.save()

            # Обработка загрузки дополнительных фотографий
            images = request.FILES.getlist('images')
            for image in images:
                RentalImage.objects.create(rental=rental, image=image)

            return redirect('rental_detail', category_name=rental.category.name, rental_id=rental.id)
    else:
        form = RentalForm(instance=rental)

    return render(request, 'edit_rental.html', {'form': form})

@login_required
def delete_rental_image(request, rental_id, image_id):
    rental = get_object_or_404(Rental, pk=rental_id, user=request.user)
    image = get_object_or_404(RentalImage, pk=image_id, rental=rental)

    # Удаление файла из системы
    if image.image:
        image.image.delete(save=False)

    # Удаление объекта RentalImage из базы данных
    image.delete()

    return redirect('edit_rental', rental_id=rental.id)


def add_to_favorites(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)

    # Проверяем, добавлено ли объявление в избранное пользователем
    favorite = Favorite.objects.filter(user=request.user, rental=rental).first()

    if favorite:
        # Если объявление уже в избранном, удаляем его из избранного
        favorite.delete()
    else:
        # Если объявление не в избранном, добавляем его в избранное
        Favorite.objects.create(user=request.user, rental=rental)

    return redirect('kino')

def favorite_rentals(request):
    favorites = Favorite.objects.filter(user=request.user)
    context = {'favorites': favorites}
    return render(request, 'favorite_rentals.html', context)

def remove_favorite(request, favorite_id):
    favorite = get_object_or_404(Favorite, id=favorite_id, user=request.user)
    favorite.delete()
    return redirect('favorite_rentals')








