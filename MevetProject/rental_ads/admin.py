from django.contrib import admin
from .models import Category, Rental, RentalImage, Contact

admin.site.register(Category)
admin.site.register(Rental)
admin.site.register(RentalImage)
admin.site.register(Contact)