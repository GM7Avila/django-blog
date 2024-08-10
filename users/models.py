import random
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')
  bio = models.CharField(max_length=40)

  def save(self, *args, **kwargs):
    if not self.pk:
      default_images = [
        'default.jpg',
        'default2.jpg',
        'default3.jpg',
        'default4.jpg',
      ]

      # Escolhe uma imagem aleatória da lista
      self.image.name = random.choice(default_images)
    super().save(*args, **kwargs)

  def __str__(self):
    return f'{self.user.username} Profile'