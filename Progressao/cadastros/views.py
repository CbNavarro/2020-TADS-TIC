from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Tipo, Usuario, Funcionario, Categoria, Produto, Venda

from django.urls import reverse_lazy

# Create your views here.


# ==================================== CREATE =============================================
class TipoCreate(CreateView):
	model = Tipo
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index')

class UsuarioCreate(CreateView):
	model = Usuario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index')

class FuncionarioCreate(CreateView):
	model = Funcionario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'salario', 'dt_hr_admicao', 'dt_hr_demicao', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index')
    
class CategoriaCreate(CreateView):
	model = Categoria
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index')

class ProdutoCreate(CreateView):
	model = Produto
	fields = ['nome', 'valor', 'categoria']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index')    

class VendaCreate(CreateView):
	model = Venda
	fields = ['dt_hr_compra', 'usuario', 'funcionario', 'produto']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index') 

# ================================================================================================
# ==================================== UPDATE ====================================================

class TipoUpdate(UpdateView):
	model = Tipo
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index')

class UsuarioUpdate(UpdateView):
	model = Usuario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index')

class FuncionarioUpdate(UpdateView):
	model = Funcionario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'salario', 'dt_hr_admicao', 'dt_hr_demicao', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index')
    
class CategoriaUpdate(UpdateView):
	model = Categoria
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index')

class ProdutoUpdate(UpdateView):
	model = Produto
	fields = ['nome', 'valor', 'categoria']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index')    

class VendaUpdate(UpdateView):
	model = Venda
	fields = ['dt_hr_compra', 'usuario', 'funcionario', 'produto']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('index') 

# ================================================================================================