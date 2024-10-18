# admin.py
from django.contrib import admin
from .models import NoteModel


class NoteAdmin(admin.ModelAdmin):
    list_display = ('user','email','title', 'date', 'content')
    list_filter = ('user', 'date',)
    search_fields = ('title', 'content','email')
admin.site.register(NoteModel, NoteAdmin)