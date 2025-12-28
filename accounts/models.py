from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.timezone import now

class User(AbstractUser):
    date_joined = models.DateTimeField(default=now)  # Uses UTC but converts to IST on display
# Ensures correct local time is stored


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')  # Ensure this exists
    bio = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.user.username




    @property
    def profile_image_url(self):
        """Return profile image URL or default placeholder"""
        if self.profile_picture:
            return self.profile_picture.url
        return settings.MEDIA_URL + "default.jpg"  # Ensure a valid default image exists
