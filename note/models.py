# models.py
from django.db import models
from django.contrib.auth.models import User
from django.forms import EmailField


class NoteModel(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)


    def __str__(self):
        return self.title
