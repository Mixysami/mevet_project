from django import forms
from .models import Rental, Category, RentalImage

from multiupload.fields import MultiFileField

class RentalForm(forms.ModelForm):
    images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5, required=False)

    class Meta:
        model = Rental
        fields = ['category', 'title', 'description', 'address', 'price', 'contact', 'main_image', 'images']
        widgets = {
            'category': forms.Select(choices=Category.objects.all(), attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'main_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

        def clean_images(self):
            images = self.cleaned_data.get('images', [])
            instance = self.instance
            if instance.pk:  # Если редактируется существующее объявление
                existing_images = instance.images.all()
                for image in existing_images:
                    if image.image not in images:
                        image.delete()
            return images