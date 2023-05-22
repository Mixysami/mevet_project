from pathlib import Path
from django.conf import settings
from django.db import models
import os
import uuid
import re
from django.contrib.auth.models import User

def rental_image_upload_path(instance, filename):
    # Get the file extension
    ext = os.path.splitext(filename)[-1].lower()
    # Create a unique filename using UUID
    unique_filename = f"{uuid.uuid4()}{ext}"
    # Sanitize the rental name
    rental_name_sanitized = re.sub(r"[^\w\-_]", "_", instance.rental.title)
    # Define the folder structure
    folder = f"rental_images/{rental_name_sanitized}_{instance.rental.id}/"
    # Return the full path
    return os.path.join(folder, unique_filename)


def rental_main_image_upload_path(instance, filename):
    ext = os.path.splitext(instance.main_image.name)[-1].lower()
    unique_filename = f"{uuid.uuid4()}{ext}"
    rental_name_sanitized = re.sub(r"[^\w\-_]", "_", instance.title)
    folder = f"rental_images/{rental_name_sanitized}_{instance.id}/main/"
    return os.path.join(folder, unique_filename)


def get_random_image_from_folder(folder):
    folder_path = Path(settings.MEDIA_ROOT, folder)
    if folder_path.exists() and folder_path.is_dir():
        images = list(folder_path.glob('*.png')) + list(folder_path.glob('*.jpg')) + list(folder_path.glob('*.jpeg'))
        if images:
            return os.path.relpath(images[0], settings.MEDIA_ROOT).replace('\\', '/')
    return None


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Rental(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    main_image = models.ImageField(upload_to=rental_main_image_upload_path, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    views_count = models.IntegerField(default=0)


    class Meta:
        verbose_name = "Rental"
        verbose_name_plural = "Rentals"

    def save(self, *args, **kwargs):
        is_new = not self.pk

        if is_new:
            # Save the rental once to generate the ID
            super(Rental, self).save(*args, **kwargs)

        if not self.main_image:
            # Try to get a random image from the corresponding folder
            folder = f"rental_images/{self.title}_{self.id}/"
            random_image_path = get_random_image_from_folder(folder)

            if random_image_path:
                self.main_image = random_image_path
            else:
                # There is no image in the folder, use the default
                self.main_image = "rental_images/default_main_image.png"
        else:
            # Save the main image with the correct path
            main_image = self.main_image
            self.main_image = None
            super(Rental, self).save(*args, **kwargs)
            self.main_image = main_image

        # Save the rental again with the updated main_image
        super(Rental, self).save(*args, **kwargs)

    def add_to_favorites(self, user):
        favorite, created = Favorite.objects.get_or_create(user=user, rental=self)
        return favorite

    def remove_from_favorites(self, user):
        Favorite.objects.filter(user=user, rental=self).delete()

    def is_favorite(self, user):
        return Favorite.objects.filter(user=user, rental=self).exists()

    def __str__(self):
        return self.title


class RentalImage(models.Model):
    rental = models.ForeignKey(Rental, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=rental_image_upload_path, blank=True, null=True)

    class Meta:
        verbose_name = "Rental Image"
        verbose_name_plural = "Rental Images"

    def __str__(self):
        return f"{self.rental.title} - Image {self.pk}"


class Contact(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, related_name='contacts')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.rental.title} - Contact {self.pk}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
        unique_together = ('user', 'rental')  # Prevents duplicates

    def __str__(self):
        return f"{self.user.username} - {self.rental.title}"

