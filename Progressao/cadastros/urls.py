from django.urls import path

# Importa as views que a gente criou 
from .views import TipoCreate, UsuarioCreate, FuncionarioCreate, CategoriaCreate, ProdutoCreate, VendaCreate

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    # Todo path tem endereço, sua_view.as_view() e nome
    path('cadastrar/tipo', TipoCreate.as_view(), name='cadastrar-tipo'),
    path('cadastrar/usuario', UsuarioCreate.as_view(), name='cadastrar-usuario'),
    path('cadastrar/funcionario', FuncionarioCreate.as_view(), name='cadastrar-funcionario'),
    path('cadastrar/categoria', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastrar/produto', ProdutoCreate.as_view(), name='cadastrar-produto'),
    path('cadastrar/venda', VendaCreate.as_view(), name='cadastrar-venda'),
]
