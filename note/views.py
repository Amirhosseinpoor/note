from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormMixin, CreateView
from .models import NoteModel
from .forms import DateFilterForm, NoteForm
from django.utils.dateparse import parse_date
from django.http import Http404


class WelcomeView(TemplateView):
    template_name = 'welcome.html'


class NoteView(CreateView):
    model = NoteModel
    form_class = NoteForm
    template_name = 'home.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        return super().form_valid(form)


class ShowView(FormMixin, ListView):
    model = NoteModel
    template_name = 'show.html'
    context_object_name = 'notes'
    form_class = DateFilterForm
    ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)

        date_str = self.request.GET.get('date')

        if date_str:
            date_obj = parse_date(date_str)

            queryset = queryset.filter(date__date=date_obj)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form(self.form_class)
        return context
