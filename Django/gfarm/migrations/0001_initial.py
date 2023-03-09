# Generated by Django 2.2.7 on 2019-11-20 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gfarm.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacao', models.CharField(help_text='Brinco do Animal', max_length=15)),
                ('marcacao', models.CharField(help_text='Sigla da Fazenda ou nome Fazenda', max_length=100, verbose_name='Marcação')),
                ('sexo', models.CharField(choices=[('Macho', 'Macho'), ('Femea', 'Femea')], max_length=10, verbose_name='Sexo Do Animal')),
                ('dataNascimento', models.DateField(verbose_name='Data Nascimento')),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaMedicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipomedicamento', models.CharField(max_length=100, verbose_name='Categoria Medicamento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaPessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50, verbose_name='Categoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fazenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('complemento', models.CharField(max_length=100)),
                ('hectares', models.FloatField(verbose_name='Hectares')),
                ('cidade', models.CharField(max_length=50)),
                ('uf', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA', 'BA'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='UF')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('nome', 'usuario')},
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local', models.CharField(max_length=50, verbose_name='Armazém')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Fazenda', verbose_name='Fazenda')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(help_text='Fornecedor', max_length=100, verbose_name='Fabricante')),
                ('qtde_estoque', models.FloatField(help_text='Quantidade do Produto em Estoque no momento', verbose_name='Quantidade em estoque')),
                ('novaCompra', models.FloatField(blank=True, help_text='Informe a quantidade comprada', null=True, verbose_name='Quantidade de medicamentos Comprada')),
                ('principio_ativo', models.TextField(max_length=100, verbose_name=' Principio Ativo')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Local', verbose_name='Barracão')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Fazenda', verbose_name='Fazenda')),
                ('tipomedicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.CategoriaMedicamento', verbose_name='Tipo medicamento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100)),
                ('soma', models.CharField(max_length=100)),
                ('mensagem', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vacinacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVacina', models.DateField(verbose_name='Data da vacinação')),
                ('dataVencimento', models.DateField(verbose_name='Data de vencimento')),
                ('observacao', models.TextField(verbose_name='Observação sobre a vacina')),
                ('animal', models.ForeignKey(help_text='Buscar por identificação, sexo, raça e pelagem', on_delete=django.db.models.deletion.PROTECT, to='gfarm.Animal', verbose_name='Animal')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Medicamento')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Fazenda', verbose_name='Fazenda')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pesagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataPesagem', models.DateField(verbose_name=' Dia Da Pesagem ')),
                ('peso', models.FloatField(verbose_name=' Peso ')),
                ('animal', models.ForeignKey(help_text='Buscar por identificação, sexo, raça e pelagem', on_delete=django.db.models.deletion.PROTECT, to='gfarm.Animal', verbose_name='Animal')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Fazenda', verbose_name='Fazenda')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Novaquantidade', models.FloatField(verbose_name='Nova Quantidade')),
                ('qtde_estoqueAtual', models.FloatField(help_text='Quantidade do Produto em Estoque no momento', verbose_name='Quantidade Em Estoque')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Medicamento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaAlimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoriaAlimento', models.CharField(max_length=20, verbose_name=' Categoria do alimento ')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalRaca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raca', models.CharField(max_length=100, verbose_name=' Raça ')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalPelagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelagem', models.CharField(max_length=20, verbose_name=' Pelagem ')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100, verbose_name=' Categoria ')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.AnimalCategoria', verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='animal',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Fazenda', verbose_name='Fazenda'),
        ),
        migrations.AddField(
            model_name='animal',
            name='pelagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.AnimalPelagem', verbose_name='Pelagem'),
        ),
        migrations.AddField(
            model_name='animal',
            name='raca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.AnimalRaca', verbose_name='Raça'),
        ),
        migrations.AddField(
            model_name='animal',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100, verbose_name='Nome Do Produto')),
                ('qtde_estoque', models.FloatField(verbose_name='Quantidade em Estoque')),
                ('principioAtivo', models.TextField(max_length=200, null=True, verbose_name='Descrição')),
                ('categoriaAlimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.CategoriaAlimento', verbose_name='Categoria Alimento')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Local', verbose_name='Barracão')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Fazenda', verbose_name='Fazenda')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pessoa', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('rg', models.CharField(max_length=14, verbose_name='RG')),
                ('cpf', models.CharField(max_length=14, validators=[gfarm.validators.validate_CPF], verbose_name='CPF')),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Feminino')], max_length=10)),
                ('dataNascimento', models.DateField(verbose_name='Data Nascimento')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('telefone', models.CharField(help_text='(xx)xxxx-xxxx', max_length=20, verbose_name='Telefone')),
                ('uf', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA', 'BA'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=2, verbose_name='UF')),
                ('cidade', models.CharField(max_length=50, verbose_name='Cidade')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.CategoriaPessoa', verbose_name='Função')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gfarm.Fazenda', verbose_name='Fazenda')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('email', 'usuario'), ('telefone', 'usuario'), ('nome_pessoa', 'usuario'), ('cpf', 'usuario'), ('rg', 'usuario')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='animal',
            unique_together={('identificacao', 'usuario')},
        ),
    ]
