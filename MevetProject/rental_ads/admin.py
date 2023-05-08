from django.contrib import admin
from .models import Rental, Category, RentalImage, Contact  # Add other models as needed

admin.site.register(Category)
admin.site.register(RentalImage)
admin.site.register(Contact)


class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'address', 'price', 'contact', 'created_at', 'updated_at')

admin.site.register(Rental, RentalAdmin)