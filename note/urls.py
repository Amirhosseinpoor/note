
from django.urls import path
from .views import NoteView, ShowView, WelcomeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('note/', NoteView.as_view(), name='home'),
    path('show/', ShowView.as_view(), name='show'),
    path('',WelcomeView.as_view(), name='welcome'),
]
