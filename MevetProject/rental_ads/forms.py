from django import forms
from .models import Rental, Category


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['category', 'title', 'description', 'address', 'price', 'contact', 'main_image']
        widgets = {'category': forms.Select(choices=Category.objects.all())}