from django.db import models

# Create your models here.

class Tipo(models.Model):
    cod_tipo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, verbose_name='Tipo de pessoa')

    def __str__ (self):
        return str(self.cod_tipo) + " - " + self.nome


class Usuario(models.Model):
    cod_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, verbose_name='Nome do Usuario')
    cpf = models.CharField(max_length=11, verbose_name='CPF do Usuario')
    dt_nascimento = models.CharField(max_length=11, verbose_name='Data de nascimento')
    email = models.CharField(max_length=50, verbose_name='Email do Usuario')
    senha = models.CharField(max_length=150, verbose_name='Senha')
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.cod_usuario) + " - " + self.nome

class Funcionario(models.Model):
    cod_funcionario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, verbose_name='Nome do Usuario')
    cpf = models.CharField(max_length=11, verbose_name='CPF do Usuario')
    dt_nascimento = models.CharField(max_length=11, verbose_name='Data de nascimento')
    email = models.CharField(max_length=50, verbose_name='Email do Usuario')
    senha = models.CharField(max_length=150, verbose_name='Senha')
    salario = models.FloatField(max_length=1000, verbose_name='Salario')
    dt_hr_admicao = models.DateTimeField()
    dt_hr_demicao = models.DateTimeField()
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.cod_funcionario) + " - " + self.nome

class Categoria(models.Model):
    cod_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, verbose_name='Nome da categoria')

    def __str__(self):
        return str(self.cod_categoria) + " - " + self.nome


class Produto(models.Model):
    cod_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, verbose_name='Nome do Produto')
    valor = models.FloatField(max_length=1000, verbose_name='Valor do Produto')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return "Categoria " + self.categoria.nome + ": " + str(self.cod_produto) + " - " + self.nome + " - " + self.valor

class Venda(models.Model):
    cod_venda = models.AutoField(primary_key=True)
    dt_hr_compra = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.cod_venda) + " - " + self.dt_hr_compra + " - " + self.produto.nome
