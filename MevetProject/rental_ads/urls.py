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
    path('add_rental/', views.add_rental, name='add_rental'),
    path('rental_manage/', views.rental_manage, name='rental_manage'),
    path('rental/<int:rental_id>/delete/', views.delete_rental, name='delete_rental'),
    path('rental/<int:rental_id>/edit/', views.edit_rental, name='edit_rental'),
    path('rental/<int:rental_id>/delete_image/<int:image_id>/', views.delete_rental_image, name='delete_rental_image'),
    path('favorites/', views.favorite_rentals, name='favorite_rentals'),
    path('favorites/add/<int:rental_id>/', views.add_favorite, name='add_favorite'),
    path('favorites/remove/<int:rental_id>/', views.remove_favorite, name='remove_favorite'),
    path('messages/', views.messages, name='messages'),
    path('messages/<int:rental_id>/messages_detail', views.messages_detail, name='messages_detail'),
    path('messages/<int:message_id>/delete/', views.delete_message, name='delete_message'),
    path('<int:rental_id>/send_message/', views.send_message, name='send_message'),

]