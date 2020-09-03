from django.urls import path

# Importa as views que a gente criou 
from .views import TipoCreate, UsuarioCreate, FuncionarioCreate, CategoriaCreate, ProdutoCreate, VendaCreate
from .views import TipoUpdate, UsuarioUpdate, FuncionarioUpdate, CategoriaUpdate, ProdutoUpdate, VendaUpdate
# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    # Todo path tem endereço, sua_view.as_view() e nome
    path('cadastrar/tipo', TipoCreate.as_view(), name='cadastrar-tipo'),
    path('cadastrar/usuario', UsuarioCreate.as_view(), name='cadastrar-usuario'),
    path('cadastrar/funcionario', FuncionarioCreate.as_view(), name='cadastrar-funcionario'),
    path('cadastrar/categoria', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('cadastrar/produto', ProdutoCreate.as_view(), name='cadastrar-produto'),
    path('cadastrar/venda', VendaCreate.as_view(), name='cadastrar-venda'),

    path('editar/tipo/<int:pk>/', TipoUpdate.as_view(), name='editar-tipo'),
    path('editar/usuario/<int:pk>/', UsuarioUpdate.as_view(), name='editar-usuario'),
    path('editar/funcionario/<int:pk>/', FuncionarioUpdate.as_view(), name='editar-funcionario'),
    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar-categoria'),
    path('editar/produto/<int:pk>/', ProdutoUpdate.as_view(), name='editar-produto'),
    path('editar/venda/<int:pk>/', VendaUpdate.as_view(), name='editar-venda'),
]
