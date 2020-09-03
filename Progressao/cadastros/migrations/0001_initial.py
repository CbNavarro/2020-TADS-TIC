# Generated by Django 2.2.12 on 2020-09-03 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('cod_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome da categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('cod_funcionario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Usuario')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF do Usuario')),
                ('dt_nascimento', models.CharField(max_length=11, verbose_name='Data de nascimento')),
                ('email', models.CharField(max_length=50, verbose_name='Email do Usuario')),
                ('senha', models.CharField(max_length=150, verbose_name='Senha')),
                ('salario', models.FloatField(max_length=1000, verbose_name='Salario')),
                ('dt_hr_admicao', models.DateTimeField()),
                ('dt_hr_demicao', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('cod_produto', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Produto')),
                ('valor', models.FloatField(max_length=1000, verbose_name='Valor do Produto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('cod_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, verbose_name='Tipo de pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cod_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Usuario')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF do Usuario')),
                ('dt_nascimento', models.CharField(max_length=11, verbose_name='Data de nascimento')),
                ('email', models.CharField(max_length=50, verbose_name='Email do Usuario')),
                ('senha', models.CharField(max_length=150, verbose_name='Senha')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('cod_venda', models.AutoField(primary_key=True, serialize=False)),
                ('dt_hr_compra', models.DateTimeField()),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Funcionario')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Produto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.Tipo'),
        ),
    ]
