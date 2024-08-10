import random
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=40, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            default_images = [
                'default.jpg',
                'default2.jpg',
                'default3.jpg',
                'default4.jpg',
            ]

            if not self.image.name or self.image.name == 'profile_pics/default.jpg':
                self.image.name = random.choice(default_images)
            
            if not self.bio:
                self.bio = "Hello, there!"

        super().save(*args, **kwargs)

        # Redimensiona a imagem se for maior que 300x300
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} Profile'