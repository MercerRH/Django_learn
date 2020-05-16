from django.db import models
from Login.models import User
# Create your models here.


class Event(models.Model):
    """事件模型类"""
    user_id = models.ForeignKey('Login.User')
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
