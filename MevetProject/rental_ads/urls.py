from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('kino/', views.kino, name='kino'),
    path('kon/', views.kon, name='kon'),
    path('pagefoto/', views.pagefoto, name='pagefoto'),
    path('svadba/', views.svadba, name='svadba'),
    path('banket/', views.banket, name='banket'),
    path('<str:category_name>/<int:rental_id>/', views.rental_detail, name='rental_detail'),
    path('search/', views.rental_search, name='rental_search'),
    path('favorites/', views.favorites, name='favorites'),
    path('add_rental/', views.add_rental, name='add_rental'),
    path('rental_manage/', views.rental_manage, name='rental_manage'),



]