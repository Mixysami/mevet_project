from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Rental, Category, RentalImage
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import RentalForm
from .models import Favorite
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Message


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('rental_manage')
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


def room(request):
    room_category = Category.objects.get(name='room')
    rental_list = Rental.objects.filter(category=room_category)
    # Получение списка идентификаторов объявлений, добавленных в избранное текущим пользователем
    if request.user.is_authenticated:  # Проверка, аутентифицирован ли пользователь
        favorite_rentals = Favorite.objects.filter(user=request.user).values_list('rental_id', flat=True)
    else:
        favorite_rentals = []  # Если пользователь не аутентифицирован, присвоить пустой список


    # Добавление флага is_favorite в контекст для каждого объявления
    for rental in rental_list:
        rental.is_favorite = rental.id in favorite_rentals
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
        "selected_filter": filter_value,
        "user": request.user,
        "favorite": Favorite.objects.filter(user=request.user) if request.user.is_authenticated else []
        # Добавление избранных объявлений в контекст, если пользователь аутентифицирован
    }
    return render(request, 'room.html', context)


def corporate(request):
    corporate_category = Category.objects.get(name='corporate')
    rental_list = Rental.objects.filter(category=corporate_category)
    # Получение списка идентификаторов объявлений, добавленных в избранное текущим пользователем
    if request.user.is_authenticated:  # Проверка, аутентифицирован ли пользователь
        favorite_rentals = Favorite.objects.filter(user=request.user).values_list('rental_id', flat=True)
    else:
        favorite_rentals = []  # Если пользователь не аутентифицирован, присвоить пустой список

    # Добавление флага is_favorite в контекст для каждого объявления
    for rental in rental_list:
        rental.is_favorite = rental.id in favorite_rentals
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
        "selected_filter": filter_value,
        "user": request.user,
        "favorite": Favorite.objects.filter(user=request.user) if request.user.is_authenticated else []
        # Добавление избранных объявлений в контекст, если пользователь аутентифицирован
    }
    return render(request, 'corporate.html', context)

def conferences(request):
    conferences_category = Category.objects.get(name='conferences')
    rental_list = Rental.objects.filter(category=conferences_category)
    # Получение списка идентификаторов объявлений, добавленных в избранное текущим пользователем
    if request.user.is_authenticated:  # Проверка, аутентифицирован ли пользователь
        favorite_rentals = Favorite.objects.filter(user=request.user).values_list('rental_id', flat=True)
    else:
        favorite_rentals = []  # Если пользователь не аутентифицирован, присвоить пустой список

    # Добавление флага is_favorite в контекст для каждого объявления
    for rental in rental_list:
        rental.is_favorite = rental.id in favorite_rentals
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
        "selected_filter": filter_value,
        "user": request.user,
        "favorite": Favorite.objects.filter(user=request.user) if request.user.is_authenticated else []
        # Добавление избранных объявлений в контекст, если пользователь аутентифицирован
    }
    return render(request, 'conferences.html', context)

def wedding(request):
    wedding_category = Category.objects.get(name='wedding')
    rental_list = Rental.objects.filter(category=wedding_category)
    # Получение списка идентификаторов объявлений, добавленных в избранное текущим пользователем
    if request.user.is_authenticated:  # Проверка, аутентифицирован ли пользователь
        favorite_rentals = Favorite.objects.filter(user=request.user).values_list('rental_id', flat=True)
    else:
        favorite_rentals = []  # Если пользователь не аутентифицирован, присвоить пустой список

    # Добавление флага is_favorite в контекст для каждого объявления
    for rental in rental_list:
        rental.is_favorite = rental.id in favorite_rentals
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
        "selected_filter": filter_value,
        "user": request.user,
        "favorite": Favorite.objects.filter(user=request.user) if request.user.is_authenticated else []
        # Добавление избранных объявлений в контекст, если пользователь аутентифицирован
    }
    return render(request, 'wedding.html', context)

def birthday(request):
    birthday_category = Category.objects.get(name='birthday')
    rental_list = Rental.objects.filter(category=birthday_category)
    # Получение списка идентификаторов объявлений, добавленных в избранное текущим пользователем
    if request.user.is_authenticated:  # Проверка, аутентифицирован ли пользователь
        favorite_rentals = Favorite.objects.filter(user=request.user).values_list('rental_id', flat=True)
    else:
        favorite_rentals = []  # Если пользователь не аутентифицирован, присвоить пустой список

    # Добавление флага is_favorite в контекст для каждого объявления
    for rental in rental_list:
        rental.is_favorite = rental.id in favorite_rentals
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
        "selected_filter": filter_value,
        "user": request.user,
        "favorite": Favorite.objects.filter(user=request.user) if request.user.is_authenticated else []
        # Добавление избранных объявлений в контекст, если пользователь аутентифицирован
    }
    return render(request, 'birthday.html', context)

def concerts(request):
    concerts_category = Category.objects.get(name='concerts')
    rental_list = Rental.objects.filter(category=concerts_category)
    # Получение списка идентификаторов объявлений, добавленных в избранное текущим пользователем
    if request.user.is_authenticated:  # Проверка, аутентифицирован ли пользователь
        favorite_rentals = Favorite.objects.filter(user=request.user).values_list('rental_id', flat=True)
    else:
        favorite_rentals = []  # Если пользователь не аутентифицирован, присвоить пустой список

    # Добавление флага is_favorite в контекст для каждого объявления
    for rental in rental_list:
        rental.is_favorite = rental.id in favorite_rentals
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
        "selected_filter": filter_value,
        "user": request.user,
        "favorite": Favorite.objects.filter(user=request.user) if request.user.is_authenticated else []
        # Добавление избранных объявлений в контекст, если пользователь аутентифицирован
    }
    return render(request, 'concerts.html', context)

def other(request):
    other_category = Category.objects.get(name='other')
    rental_list = Rental.objects.filter(category=other_category)
    # Получение списка идентификаторов объявлений, добавленных в избранное текущим пользователем
    if request.user.is_authenticated:  # Проверка, аутентифицирован ли пользователь
        favorite_rentals = Favorite.objects.filter(user=request.user).values_list('rental_id', flat=True)
    else:
        favorite_rentals = []  # Если пользователь не аутентифицирован, присвоить пустой список

    # Добавление флага is_favorite в контекст для каждого объявления
    for rental in rental_list:
        rental.is_favorite = rental.id in favorite_rentals
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
        "selected_filter": filter_value,
        "user": request.user,
        "favorite": Favorite.objects.filter(user=request.user) if request.user.is_authenticated else []
        # Добавление избранных объявлений в контекст, если пользователь аутентифицирован
    }
    return render(request, 'other.html', context)

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

    if request.user.is_authenticated:
        favorite_rentals = Favorite.objects.filter(user=request.user).values_list('rental_id', flat=True)
    else:
        favorite_rentals = []

    for rental in rental_list:
        rental.is_favorite = rental.id in favorite_rentals

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
    rental_list = Rental.objects.filter(user=user).prefetch_related('message_set')
    username = user.username

    for rental in rental_list:
        rental.message_count = rental.message_set.count()

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

@login_required
def favorite_rentals(request):
    favorites = Favorite.objects.filter(user=request.user)
    context = {'favorites': favorites}
    return render(request, 'favorite_rentals.html', context)


@login_required
@require_POST
def add_favorite(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    Favorite.objects.get_or_create(user=request.user, rental=rental)
    return JsonResponse({'status': 'success'})


@login_required
@require_POST
def remove_favorite(request, rental_id):
    favorite = get_object_or_404(Favorite, rental_id=rental_id, user=request.user)
    favorite.delete()
    return JsonResponse({'message': 'Успешно удалено из избранного'})


from django.shortcuts import redirect

@login_required
def send_message(request, rental_id):
    if request.method == 'POST':
        message_text = request.POST['message']
        rental = get_object_or_404(Rental, id=rental_id)
        recipient = rental.user
        sender = request.user
        message = Message.objects.create(
            sender=sender,
            recipient=recipient,
            rental=rental,
            message=message_text
        )
        return redirect('messages_detail', rental_id=rental.id)  # Изменено на 'messages_detail'
    else:
        rental = get_object_or_404(Rental, id=rental_id)
        return render(request, 'send_message.html', {'rental': rental})

@login_required
def messages(request):
    user = request.user
    rental_list_received = Rental.objects.filter(message__recipient=user).distinct()
    rental_list_sent = Rental.objects.filter(message__sender=user).distinct()
    rental_list = rental_list_received | rental_list_sent
    return render(request, 'messages.html', {'rental_list': rental_list})
@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.user == message.recipient:
        message.delete()
    return redirect('messages', rental_id=message.rental.id)


@login_required
def messages_detail(request, rental_id):
    rental = get_object_or_404(Rental, id=rental_id)
    messages = Message.objects.filter(rental=rental)

    if request.method == 'POST':
        message_text = request.POST['message']
        sender = request.user
        recipient = rental.user
        message = Message.objects.create(
            sender=sender,
            recipient=recipient,
            rental=rental,
            message=message_text
        )
        return redirect('messages_detail', rental_id=rental_id)

    return render(request, 'messages_detail.html', {'rental': rental, 'messages': messages})
