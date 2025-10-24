from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from django.shortcuts import redirect
from .forms import LoginForm
from typing import Any
# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        senha = form.cleaned_data['senha']
        usuario = authenticate(self.request, username=email, password=senha)
        if usuario is not None:
            login(self.request, usuario)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.context_data['error'] = 'E-mail ou senha inválidos.'
        return response


class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect('login')
