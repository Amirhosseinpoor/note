# models.py
from django.db import models
from django.contrib.auth.models import User


class NoteModel(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
