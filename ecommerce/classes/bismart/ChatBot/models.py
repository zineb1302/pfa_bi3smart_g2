from django.db import models
from django.utils import timezone

# Create your models here.
class Chat(models.Model):
    message = models.CharField(max_length=255)
    sender = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)