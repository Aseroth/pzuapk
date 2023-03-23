from django.db import models
from django.utils import timezone

class Apk(models.Model):
    agent = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    numer = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    scope = models.TextField()

    def publish(self):
        if self.scope !='':
            self.save()

    def __str__(self):
        return self.numer


# Create your models here.
