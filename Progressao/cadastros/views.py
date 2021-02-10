from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Tipo, Usuario, Funcionario, Categoria, Produto, Venda

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404
# Create your views here.


# ==================================== CREATE =============================================
class TipoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	group_required = u"admin's"
	login_url = reverse_lazy('login')
	model = Tipo
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-tipo')

class UsuarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	group_required = u"admin's"
	login_url = reverse_lazy('login')
	model = Usuario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-usuario')

class FuncionarioCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	group_required = u"admin's"
	login_url = reverse_lazy('login')
	model = Funcionario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'salario', 'dt_hr_admicao', 'dt_hr_demicao', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-funcionario')
    
class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	group_required = u"admin's"
	login_url = reverse_lazy('login')
	model = Categoria
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-categoria')

class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	group_required = u"admin's"
	login_url = reverse_lazy('login')
	model = Produto
	fields = ['nome', 'valor', 'categoria']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-produto')    

class VendaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
	group_required = u"admin's"
	login_url = reverse_lazy('login')
	model = Venda
	fields = ['dt_hr_compra', 'usuario', 'funcionario', 'produto']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-venda') 

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		url = super().form_valid(form)
		return url

# ================================================================================================
# ==================================== UPDATE ====================================================

class TipoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
	group_required = [u"admin's", u"moder"]
	login_url = reverse_lazy('login')
	model = Tipo
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-tipo')

class UsuarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
	group_required = [u"admin's", u"moder"]
	login_url = reverse_lazy('login')
	model = Usuario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-usuario')

class FuncionarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
	group_required = [u"admin's", u"moder"]
	login_url = reverse_lazy('login')
	model = Funcionario
	fields = ['nome', 'cpf', 'dt_nascimento',
    'email', 'senha', 'salario', 'dt_hr_admicao', 'dt_hr_demicao', 'tipo']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-funcionario')
    
class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
	group_required = [u"admin's", u"moder"]
	login_url = reverse_lazy('login')
	model = Categoria
	fields = ['nome']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-categoria')

class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
	group_required = [u"admin's", u"moder"]
	login_url = reverse_lazy('login')
	model = Produto
	fields = ['nome', 'valor', 'categoria']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-produto')    

class VendaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
	group_required = [u"admin's", u"moder"]
	login_url = reverse_lazy('login')
	model = Venda
	fields = ['dt_hr_compra', 'usuario', 'funcionario', 'produto']
	template_name = 'cadastros/formularioCadastro.html'
	success_url = reverse_lazy('registros-venda') 

	def get_object(self, queryset=None):
		self.object = get_object_or_404(Venda, pk=self.kwargs['pk'], usuario=self.request.user)

		return self.object

# ================================================================================================
# ==================================== DELETE ====================================================

class TipoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
	group_required = u"admin's"
	login_url = reverse_lazy('login')
	model = Tipo
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-tipo')

class UsuarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
	group_required = u"admin's"
	login_url = reverse_lazy('login')
	model = Usuario
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-usuario')

class FuncionarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
	group_required = u"admin's"
	login_url = reverse_lazy('login')
	model = Funcionario
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-funcionario')
    
class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
	group_required = u"admin's"
	login_url = reverse_lazy('login')
	model = Categoria
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-categoria')

class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
	group_required = u"admin's"
	login_url = reverse_lazy('login')
	model = Produto
	template_name = 'cadastros/formularioCadastro-excluir.html'
	success_url = reverse_lazy('registros-produto')    

class VendaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
	group_required = u"admin's"
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

	def get_queryset(self):
		self.object_list = Venda.objects.filter(usuario=self.request.user)
		return self.object_list
