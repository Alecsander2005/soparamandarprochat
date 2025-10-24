from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ExemploForm
from .models import Exemplo


# LoginRequiredMixin é um mixin que obriga o usuário a estar logado.
class ExemploDetailView(LoginRequiredMixin, DetailView):
    # nome da classe do model.
    model = Exemplo
    # nome do template.
    template_name = 'exemplo/exemplo_detalhe.html'
    # nome da variável que vai ser usada no template.
    context_object_name = 'exemplo'


class ExemploCreateView(LoginRequiredMixin, CreateView):
    model = Exemplo
    # Formulário que será usado para criar a instância.
    form_class = ExemploForm
    template_name = 'exemplo/cadastrar_exemplo.html'
    success_url = reverse_lazy('index')


class ExemploUpdateView(LoginRequiredMixin, UpdateView):
    model = Exemplo
    form_class = ExemploForm
    template_name = 'exemplo/atualizar_exemplo.html'
    context_object_name = 'exemplo'
    success_url = reverse_lazy('index')


class ExemploListView(LoginRequiredMixin, ListView):
    model = Exemplo
    template_name = 'exemplo/exemplo_lista.html'
    context_object_name = 'exemplo'
    paginate_by = 10

    def get_queryset(self):
        # Ordene the QuerySet pelo a campo específico, for example, 'criado'
        return Exemplo.objects.all().order_by('-criado')


class ExemploDatatableView(LoginRequiredMixin, ListView):
    model = Exemplo
    template_name = 'exemplo/exemplo_datatable.html'
    context_object_name = 'exemplo'
    paginate_by = 10

    def get_queryset(self):
        # Ordene the QuerySet pelo a campo específico, for example, 'criado'
        return Exemplo.objects.all().order_by('-criado')


class ExemploDeleteView(LoginRequiredMixin, DeleteView):
    model = Exemplo
    template_name = 'exemplo/remover_exemplo.html'
    success_url = reverse_lazy('index')
