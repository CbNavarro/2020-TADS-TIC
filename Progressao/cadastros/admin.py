from django.contrib import admin

from .models import Tipo, Usuario, Funcionario, Categoria, Produto, Venda
# Register your models here.
admin.site.register(Tipo)
admin.site.register(Usuario)
admin.site.register(Funcionario)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Venda)