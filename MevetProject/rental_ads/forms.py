from django import forms
from .models import Rental, Category


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['category', 'title', 'description', 'address', 'price', 'contact', 'main_image']
        widgets = {
          'category': forms.Select(choices=Category.objects.all(), attrs={'class': 'form-control'}),
          'title': forms.TextInput(attrs={'class': 'form-control'}),
          'description': forms.Textarea(attrs={'class': 'form-control'}),
          'address': forms.TextInput(attrs={'class': 'form-control'}),
          'price': forms.NumberInput(attrs={'class': 'form-control'}),
          'contact': forms.TextInput(attrs={'class': 'form-control'}),
          'main_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }