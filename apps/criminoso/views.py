from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from .forms import CardCriminosoForm, TimeUsuarioForm, UsuarioForm
from .models import CardCriminoso, TimeUsuario, Usuario


class CardCriminosoView(FormView):
    template_name = "cardcriminoso/cardcriminoso.html"
    form_class = CardCriminosoForm

class CardCriminosoListView(LoginRequiredMixin, ListView):
    model = CardCriminoso
    template_name = 'cardcriminoso/cardcriminoso_listar.html'
    context_object_name = 'cards_criminosos'
    paginate_by = 30

    def get_queryset(self):
        return CardCriminoso.objects.filter(ativo=True)

class CardCriminosoDetailView(LoginRequiredMixin, DetailView):
    model = CardCriminoso
    template_name = 'cardcriminoso/cardcriminoso_detalhe.html'
    context_object_name = 'card_criminoso'
    
class CardCriminosoCreateView(LoginRequiredMixin, CreateView):
    model = CardCriminoso
    form_class = CardCriminosoForm
    template_name = 'cardcriminoso/cardcriminoso_cadastrar.html'
    success_url = reverse_lazy('criminoso:card_criminoso')

class CardCriminosoUpdateView(LoginRequiredMixin, UpdateView):
    model = CardCriminoso
    form_class = CardCriminosoForm
    template_name = 'cardcriminoso/cardcriminoso_atualizar.html'
    context_object_name = 'criminoso'
    success_url = reverse_lazy('criminoso:card_criminoso')

class CardCriminosoDeleteView(LoginRequiredMixin, DeleteView):
    model = CardCriminoso
    template_name = 'cardcriminoso/cardcriminoso_deletar.html'
    context_object_name = 'criminoso'
    success_url = reverse_lazy('criminoso:card_criminoso')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        for time in self.object.times.all():
            time.cards.remove(self.object)

        self.object.ativo = False
        self.object.save()
        return redirect(self.success_url)

class EscalarCriminosoView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        criminoso = get_object_or_404(CardCriminoso, pk=pk)

        if 'criminosos_escalados_ids' not in request.session:
            request.session['criminosos_escalados_ids'] = []

        if criminoso.id not in request.session['criminosos_escalados_ids']:
            if len(request.session['criminosos_escalados_ids']) < 10:
                request.session['criminosos_escalados_ids'].append(criminoso.id)
                request.session.modified = True
            else:
                pass

        return redirect('criminoso:time_usuario')

class TimeUsuarioView(LoginRequiredMixin, FormView):
    template_name = "timeusuario/timeusuario.html"
    form_class = TimeUsuarioForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        escalados_ids = self.request.session.get('criminosos_escalados_ids', [])
        # Filtra apenas cards ativos
        criminosos_escalados = CardCriminoso.objects.filter(id__in=escalados_ids, ativo=True)
        context['criminosos_escalados'] = list(criminosos_escalados)
        num_slots_ocupados = len(criminosos_escalados)
        num_placeholders = 10 - num_slots_ocupados
        context['num_placeholders'] = num_placeholders
        return context

class TimeUsuarioCreateView(FormView, CreateView):
    model = TimeUsuario
    template_name = 'timeusuario/timeusuario_cadastrar.html'
    form_class = TimeUsuarioForm 
    success_url = reverse_lazy('criminoso:time_usuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards_criminosos'] = CardCriminoso.objects.filter(ativo=True)
        return context
    
class TimeUsuarioListView(LoginRequiredMixin, ListView):
    model = TimeUsuario
    template_name = 'timeusuario/timeusuario_listar.html'
    context_object_name = 'times_usuario'
    paginate_by = 30

class TimeUsuarioDetailView(LoginRequiredMixin, DetailView):
    model = TimeUsuario
    template_name = 'timeusuario/timeusuario_detalhe.html'
    context_object_name = 'time_usuario'

class TimeUsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = TimeUsuario
    template_name = 'timeusuario/timeusuario_deletar.html'
    context_object_name = 'time_usuario'
    success_url = reverse_lazy('criminoso:time_listar')

class TimeUsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = TimeUsuario
    form_class = TimeUsuarioForm
    template_name = 'timeusuario/timeusuario_atualizar.html'
    context_object_name = 'time_usuario'
    success_url = reverse_lazy('criminoso:time_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cards_criminosos'] = CardCriminoso.objects.filter(ativo=True)
        return context