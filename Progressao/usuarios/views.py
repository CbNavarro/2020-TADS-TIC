from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class UsuarioCreate(CreateView):
    template_name = 'cadastros/formularioCadastro.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Cadastro de Usuario'
        context['botao'] = 'Cadastrar'
        return context

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='moder')
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url
