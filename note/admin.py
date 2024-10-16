# admin.py
from django.contrib import admin
from .models import NoteModel


class NoteAdmin(admin.ModelAdmin):
    list_display = ('user','title', 'date', 'content')
    list_filter = ('user', 'date',)
    search_fields = ('title', 'content')
admin.site.register(NoteModel, NoteAdmin)