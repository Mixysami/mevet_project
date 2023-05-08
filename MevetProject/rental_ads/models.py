from django.db import models
import os
import uuid
import re


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
    # Get the file extension
    ext = os.path.splitext(filename)[-1].lower()
    # Create a unique filename using UUID
    unique_filename = f"{uuid.uuid4()}{ext}"
    # Sanitize the rental name
    rental_name_sanitized = re.sub(r"[^\w\-_]", "_", instance.title)
    # Define the folder structure
    folder = f"rental_images/{rental_name_sanitized}_{instance.rental.id}/main/"
    # Return the full path
    return os.path.join(folder, unique_filename)


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

    class Meta:
        verbose_name = "Rental"
        verbose_name_plural = "Rentals"

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
