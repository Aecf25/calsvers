from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=255)
    password = models.TextField()
    email = models.TextField()
    def __str__(self):
        return self.username