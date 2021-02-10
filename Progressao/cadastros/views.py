from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Tipo, Usuario, Funcionario, Categoria, Produto, Venda

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# ==================================== CREATE =============================================
class TipoCreate(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	model = Tipo
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-tipo')

class UsuarioCreate(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	model = Usuario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-usuario')

class FuncionarioCreate(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	model = Funcionario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'salario', 'dt_hr_admicao', 'dt_hr_demicao', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-funcionario')
    
class CategoriaCreate(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	model = Categoria
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-categoria')

class ProdutoCreate(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	model = Produto
	fields = ['nome', 'valor', 'categoria']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-produto')    

class VendaCreate(LoginRequiredMixin, CreateView):
	login_url = reverse_lazy('login')
	model = Venda
	fields = ['dt_hr_compra', 'usuario', 'funcionario', 'produto']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-venda') 

# ================================================================================================
# ==================================== UPDATE ====================================================

class TipoUpdate(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	model = Tipo
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-tipo')

class UsuarioUpdate(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	model = Usuario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-usuario')

class FuncionarioUpdate(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	model = Funcionario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'salario', 'dt_hr_admicao', 'dt_hr_demicao', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-funcionario')
    
class CategoriaUpdate(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	model = Categoria
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-categoria')

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	model = Produto
	fields = ['nome', 'valor', 'categoria']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-produto')    

class VendaUpdate(LoginRequiredMixin, UpdateView):
	login_url = reverse_lazy('login')
	model = Venda
	fields = ['dt_hr_compra', 'usuario', 'funcionario', 'produto']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-venda') 

# ================================================================================================
# ==================================== DELETE ====================================================

class TipoDelete(LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	model = Tipo
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-tipo')

class UsuarioDelete(LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	model = Usuario
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-usuario')

class FuncionarioDelete(LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	model = Funcionario
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-funcionario')
    
class CategoriaDelete(LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	model = Categoria
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-categoria')

class ProdutoDelete(LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	model = Produto
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-produto')    

class VendaDelete(LoginRequiredMixin, DeleteView):
	login_url = reverse_lazy('login')
	model = Venda
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-venda') 

# ================================================================================================
# ==================================== LIST ======================================================

class TipoList(ListView):
	model = Tipo
	template_name = 'cadastros/registros/tipo.html'

class UsuarioList(ListView):
	model = Usuario
	template_name = 'cadastros/registros/usuario.html'

class FuncionarioList(ListView):
	model = Funcionario
	template_name = 'cadastros/registros/funcionario.html'
    
class CategoriaList(ListView):
	model = Categoria
	template_name = 'cadastros/registros/categoria.html'

class ProdutoList(ListView):
	model = Produto
	template_name = 'cadastros/registros/produto.html'    

class VendaList(ListView):
	model = Venda
	template_name = 'cadastros/registros/venda.html' 