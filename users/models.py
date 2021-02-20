from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #cascade means if user is deleted, profile is deleted too
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def  __str__(self):
        return f'{self.user.username} Profile'



