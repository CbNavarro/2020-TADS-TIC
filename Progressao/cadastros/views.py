from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Tipo, Usuario, Funcionario, Categoria, Produto, Venda

from django.urls import reverse_lazy

# Create your views here.


# ==================================== CREATE =============================================
class TipoCreate(CreateView):
	model = Tipo
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-tipo')

class UsuarioCreate(CreateView):
	model = Usuario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-usuario')

class FuncionarioCreate(CreateView):
	model = Funcionario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'salario', 'dt_hr_admicao', 'dt_hr_demicao', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-funcionario')
    
class CategoriaCreate(CreateView):
	model = Categoria
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-categoria')

class ProdutoCreate(CreateView):
	model = Produto
	fields = ['nome', 'valor', 'categoria']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-produto')    

class VendaCreate(CreateView):
	model = Venda
	fields = ['dt_hr_compra', 'usuario', 'funcionario', 'produto']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-venda') 

# ================================================================================================
# ==================================== UPDATE ====================================================

class TipoUpdate(UpdateView):
	model = Tipo
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-tipo')

class UsuarioUpdate(UpdateView):
	model = Usuario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-usuario')

class FuncionarioUpdate(UpdateView):
	model = Funcionario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'salario', 'dt_hr_admicao', 'dt_hr_demicao', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-funcionario')
    
class CategoriaUpdate(UpdateView):
	model = Categoria
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-categoria')

class ProdutoUpdate(UpdateView):
	model = Produto
	fields = ['nome', 'valor', 'categoria']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-produto')    

class VendaUpdate(UpdateView):
	model = Venda
	fields = ['dt_hr_compra', 'usuario', 'funcionario', 'produto']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-venda') 

# ================================================================================================
# ==================================== DELETE ====================================================

class TipoDelete(DeleteView):
	model = Tipo
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-tipo')

class UsuarioDelete(DeleteView):
	model = Usuario
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-usuario')

class FuncionarioDelete(DeleteView):
	model = Funcionario
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-funcionario')
    
class CategoriaDelete(DeleteView):
	model = Categoria
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-categoria')

class ProdutoDelete(DeleteView):
	model = Produto
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-produto')    

class VendaDelete(DeleteView):
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