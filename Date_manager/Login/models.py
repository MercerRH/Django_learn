from django.db import models


# Create your models here.

class User(models.Model):
    """用户类"""
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name
