from django.db import models
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        # Resize image if it exists
        if self.photo:
            img = Image.open(self.photo)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)

                # Save the image to a BytesIO object to use as a file
                img_io = io.BytesIO()
                img.save(img_io, format='JPEG', quality=85)
                img_file = InMemoryUploadedFile(
                    img_io,
                    'ImageField',
                    f"{self.photo.name.split('/')[-1].split('.')[0]}.jpg",
                    'image/jpeg',
                    img_io.tell(),
                    None
                )
                self.photo = img_file

        super().save(*args, **kwargs)