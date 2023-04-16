from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class Profile(models.Model):
    """ User Profiles Model """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.CharField(max_length=400, blank=True, null=True)
    city = models.CharField(max_length=110, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="profile_pics/%Y/%m")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        """ Override save method to resize image """
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.image.path)


class ProfileState(models.Model):
    """ User Profiles State Model """
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_state")
    state_message = models.CharField(max_length=300)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_profile)
