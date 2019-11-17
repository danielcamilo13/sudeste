from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


class cidade(models.Model):
    id = models.AutoField(primary_key=True)
    nm_cidade = models.CharField(max_length=50, blank=True, verbose_name="Cidade")

    def __str__(self):
        return self.nm_cidade

    class Meta:
        verbose_name = 'Cidade'


@python_2_unicode_compatible
class estado(models.Model):
    id = models.AutoField(primary_key=True)
    nm_estado = models.CharField(max_length=50, blank=True, verbose_name="Estado")

    def __str__(self):
        return self.nm_estado

    class Meta:
        verbose_name = 'Estado'

@python_2_unicode_compatible
class tipocacamba(models.Model):
    id = models.AutoField(primary_key=True)
    tpCacamba = models.CharField(max_length=30,blank=True,verbose_name='Tipo de Cacamba')
    def __str__(self):
        return self.tpCacamba
    class Meta:
        verbose_name='Tipos de Cacambas'

@python_2_unicode_compatible
class cacamba(models.Model):
    nrcacamba = models.AutoField(primary_key=True)
    tpCacamba = models.ForeignKey(tipocacamba,on_delete=models.CASCADE,verbose_name='Tipo de Cacamba', max_length=30, blank=True, null=True)
    espCacamba = models.CharField(max_length=100,blank=True,verbose_name='Especificacao')
    capCacamba = models.CharField(max_length=10,blank=True,verbose_name='Capacidade')
    sttCacamba = models.IntegerField(verbose_name='Status')
    tamCacamba = models.IntegerField(verbose_name='Tampa')
    traCacamba = models.IntegerField(verbose_name='Trava')
    funCacamba = models.IntegerField(verbose_name='Fundo')
    argCacamba = models.IntegerField(verbose_name='Argola')
    pinCacamba = models.IntegerField(verbose_name='Pintura')
    def __str__(self):
        return str(self.espCacamba)
    class Meta:
        verbose_name='3. Cacamba'

@python_2_unicode_compatible
class historicocacamba(models.Model):
    id = models.AutoField(primary_key=True)
    desCacamba = models.CharField(max_length=300,blank=True,verbose_name='Descricao do problema')
    date =models.DateTimeField(verbose_name='Data de Registro',default=timezone.now,null=False)
    cacamba = models.ForeignKey(cacamba,on_delete=models.CASCADE,verbose_name='Historico de cacamba',null=True)

@python_2_unicode_compatible
class identidadejuridica(models.Model):
    id = models.AutoField(primary_key=True)
    nm = models.CharField(max_length=55, blank=False, null=False, verbose_name='Razao Social')
    cnpj = models.CharField(max_length=25, blank=True, null=True)
    categoria = models.CharField(max_length=40, blank=True, null=True)
    endereco = models.CharField(max_length=90, blank=True, null=True,verbose_name='Endereco Matriz')
    num = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=70, blank=True, null=True)
    bairro = models.CharField(max_length=80, blank=True, null=True,verbose_name='Bairro')
    cep = models.CharField(max_length=15, blank=True, null=True,verbose_name='CEP Matriz')
    cidade = models.ForeignKey(cidade, on_delete=models.CASCADE, max_length=30, blank=True, null=True,verbose_name='Cidade')
    estado = models.ForeignKey(estado, on_delete=models.CASCADE, max_length=30, blank=True, null=True,verbose_name='Estado')
    pais = models.CharField(max_length=100, blank=True, null=True,verbose_name='Pais sede')
    ddd1 = models.CharField(max_length=4, blank=True, verbose_name="DDD", null=True)
    fone1 = models.CharField(max_length=15, blank=True, verbose_name="Telefone Principal", null=True)
    ddd2 = models.CharField(max_length=4, blank=True, verbose_name="DDD", null=True)
    fone2 = models.CharField(max_length=15, blank=True, verbose_name="Telefone de apoio", null=True)
    contato = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(max_length=60, blank=True, null=True,verbose_name='E-mail juridico')
    endereco_op = models.CharField(max_length=90, blank=True, null=True,verbose_name='Endereco Operacional')
    complemento_op = models.CharField(max_length=70, blank=True, null=True,verbose_name='Complemento Operacional')
    bairro_op = models.CharField(max_length=80, blank=True, null=True,verbose_name='Bairro Operacional')
    cep_op = models.CharField(max_length=15, blank=True, null=True,verbose_name='CEP Operacional')
    # cidade_op = models.ForeignKey(cidade, on_delete=models.CASCADE, max_length=30, blank=True, null=True,verbose_name='Cidade Operacional')
    # estado_op = models.ForeignKey(estado, on_delete=models.CASCADE, max_length=30, blank=True, null=True,verbose_name='Estado Operacional')
    pais_op = models.CharField(max_length=100, blank=True, null=True,verbose_name='Pais Operacional')
    ddd1_op = models.CharField(max_length=4, blank=True, verbose_name="DDD Operacional", null=True)
    fone1_op = models.CharField(max_length=15, blank=True, verbose_name="Telefone Operacional", null=True)
    nr_banco = models.IntegerField(blank=True, null=True, verbose_name='Numero do banco')
    banco = models.CharField(max_length=40, blank=True, null=True,verbose_name='Banco')
    tp_conta = models.CharField(max_length=20, blank=True, null=True,verbose_name='tipo de conta')
    agencia = models.CharField(max_length=15, blank=True, null=True,verbose_name='Agencia')
    nr_conta = models.CharField(max_length=20, blank=True, verbose_name="Número da conta", null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    obs = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nm

    class Meta:
        verbose_name = '1. Identidade Juridica'


@python_2_unicode_compatible
class colaborador(models.Model):
    id = models.AutoField(primary_key=True)
    nm_colaborador = models.CharField(max_length=55, blank=False, null=False, verbose_name='Nome do fornecedor')
    cnpj = models.CharField(max_length=25, blank=True, null=True)
    funcao = models.CharField(max_length=60, blank=True, null=True)
    endereco = models.CharField(max_length=90, blank=True, null=True)
    num = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=70, blank=True, null=True)
    bairro = models.CharField(max_length=80, blank=True, null=True)
    cep = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.ForeignKey(cidade, on_delete=models.CASCADE, max_length=30, blank=True, null=True)
    estado = models.ForeignKey(estado, on_delete=models.CASCADE, max_length=30, blank=True, null=True)
    ddd1 = models.CharField(max_length=4, blank=True, verbose_name="DDD", null=True)
    fone1 = models.CharField(max_length=15, blank=True, verbose_name="Telefone Principal", null=True)
    ddd2 = models.CharField(max_length=4, blank=True, verbose_name="DDD", null=True)
    fone2 = models.CharField(max_length=15, blank=True, verbose_name="Telefone de apoio", null=True)
    email = models.EmailField(max_length=60, blank=True, null=True)
    nr_banco = models.IntegerField(blank=True, null=True)
    banco = models.CharField(max_length=40, blank=True, null=True)
    tp_conta = models.CharField(max_length=20, blank=True, null=True)
    agencia = models.CharField(max_length=15, blank=True, null=True)
    nr_conta = models.CharField(max_length=20, blank=True, verbose_name="Número da conta", null=True)
    status = models.CharField(max_length=25, blank=True, null=True)
    obs = models.CharField(max_length=90, blank=True, null=True)

    def __str__(self):
        return self.nm_colaborador
    class Meta:
        verbose_name = '2. Colaboradores'
