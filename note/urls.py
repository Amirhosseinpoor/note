from django.contrib import admin
from django.urls import path
from .views import NoteView, ShowView

urlpatterns = [
    path('note/', NoteView.as_view(), name='home'),
    path('show/', ShowView.as_view(), name='show')
]
