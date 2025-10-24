from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ExemploImagemForm
from .models import ExemploImagens
# Create your views here.


class ImagensListView(LoginRequiredMixin, ListView):
    model = ExemploImagens
    template_name = 'imagem/exemplo_lista.html'
    context_object_name = 'imagem'
    paginate_by = 10


class ImagensDetailView(LoginRequiredMixin, DetailView):
    model = ExemploImagens
    template_name = 'imagem/exemplo_detalhe.html'
    context_object_name = 'imagem'


class ImagensCreateView(LoginRequiredMixin, CreateView):
    model = ExemploImagens
    form_class = ExemploImagemForm
    template_name = 'imagem/cadastrar_exemplo.html'
    success_url = reverse_lazy('index')


class ImagensUpdateView(LoginRequiredMixin, UpdateView):
    model = ExemploImagens
    form_class = ExemploImagemForm
    template_name = 'imagem/atualizar_exemplo.html'
    context_object_name = 'imagem'
    success_url = reverse_lazy('index')


class ImagensDeleteView(LoginRequiredMixin, DeleteView):
    model = ExemploImagens
    template_name = 'imagem/remover_exemplo.html'
    context_object_name = 'imagem'
    success_url = reverse_lazy('index')
