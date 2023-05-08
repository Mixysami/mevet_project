from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kino/', views.kino, name='kino'),
    path('kon/', views.kon, name='kon'),
    path('pagefoto/', views.pagefoto, name='pagefoto'),
    path('svadba/', views.svadba, name='svadba'),
    path('banket/', views.banket, name='banket'),
    path('<str:category_name>/<int:rental_id>/', views.rental_detail, name='rental_detail'),
]