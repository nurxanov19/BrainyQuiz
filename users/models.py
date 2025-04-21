from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users/images/', default='users/images/default.png')

    def __str__(self):
        return self.username

class Saved(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey('main.Test', on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.user.username} {self.test.title}"


