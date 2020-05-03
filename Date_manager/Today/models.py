from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    event_date = models.DateField()
    crate_date = models.DateField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
