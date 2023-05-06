from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def kino(request):
    return render(request, 'kino.html')

def kon(request):
    return render(request, 'kon.html')

def pagefoto(request):
    return render(request, 'pagefoto.html')

def svadba(request):
    return render(request, 'svadba.html')