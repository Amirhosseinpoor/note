from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormMixin, CreateView
from .models import NoteModel
from .forms import DateFilterForm, NoteForm


class NoteView(CreateView):
    model = NoteModel
    form_class = NoteForm
    template_name = 'home.html'
    success_url = reverse_lazy('show')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ShowView(FormMixin, ListView):
    model = NoteModel
    template_name = 'show.html'
    context_object_name = 'notes'
    form_class = DateFilterForm
    ordering = ['-date']
    success_url = reverse_lazy('show')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        date = self.request.POST.get('date')
        if date:
            queryset = queryset.filter(date__date=date)
        return queryset
