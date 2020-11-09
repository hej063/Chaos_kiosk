from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    photo = models.ImageField(blank=True, null=True, upload_to="core/images")
    text = models.TextField()
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    count = models.IntegerField(default=0)
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Card(models.Model):
    photo = models.ImageField(blank=True, null=True, upload_to="core/images")
    warning = models.TextField(null=True)
