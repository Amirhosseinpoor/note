from django import forms
from .models import NoteModel


class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['title', 'content', ]


class DateFilterForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
