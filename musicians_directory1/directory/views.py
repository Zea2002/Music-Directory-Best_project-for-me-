
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

class MusicianListView(ListView):
    model = Musician
    template_name = 'musician_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authenticated'] = self.request.user.is_authenticated
        return context

class MusicianDetailView(DetailView):
    model = Musician
    template_name = 'musician_detail.html'

class MusicianCreateView(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician-list')

class MusicianUpdateView(LoginRequiredMixin, UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('musician-list')

class MusicianDeleteView(LoginRequiredMixin, DeleteView):
    model = Musician
    template_name = 'musician_confirm_delete.html'
    success_url = reverse_lazy('musician-list')

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('musician-list')

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('musician-list')

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'album_confirm_delete.html'
    success_url = reverse_lazy('musician-list')
