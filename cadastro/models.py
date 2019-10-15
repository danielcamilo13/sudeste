from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class cidade(models.Model):
    id = models.AutoField(primary_key=True)
    nm_cidade = models.CharField(max_length=50,blank=True,verbose_name="Cidade")
    def __str__(self):
        return self.nm_cidade
    class Meta:
        verbose_name='2. Cidade'

@python_2_unicode_compatible
class estado(models.Model):
    id = models.AutoField(primary_key=True)
    nm_estado = models.CharField(max_length=50,blank=True,verbose_name="Estado")
    def __str__(self):
        return self.nm_estado
    class Meta:
        verbose_name='3. Estado'
        
@python_2_unicode_compatible
class cadastro_geral(models.Model):
    id = models.AutoField(primary_key=True)
    nm = models.CharField(max_length=55,blank=False,null=False,verbose_name='Nome')
    cnpj = models.CharField(max_length=25,blank=True,null=True)
    categoria = models.CharField(max_length=40,blank=True,null=True)
    endereco = models.CharField(max_length=90,blank=True,null=True)
    num = models.CharField(max_length=10,blank=True,null=True)
    complemento = models.CharField(max_length=70,blank=True,null=True)
    bairro = models.CharField(max_length=80,blank=True,null=True)
    cep = models.CharField(max_length=15,blank=True,null=True)
    cidade = models.ForeignKey(cidade,on_delete=models.CASCADE,max_length=30,blank=True,null=True)
    estado = models.ForeignKey(estado,on_delete=models.CASCADE,max_length=30,blank=True,null=True)
    ddd1 = models.CharField(max_length=4,blank=True,verbose_name="DDD",null=True)
    fone1 = models.CharField(max_length=15,blank=True, verbose_name="Telefone Principal",null=True)
    ddd2 = models.CharField(max_length=4,blank=True, verbose_name="DDD",null=True)
    fone2 = models.CharField(max_length=15,blank=True,verbose_name="Telefone de apoio",null=True)
    contato = models.CharField(max_length=60,blank=True,null=True)
    email = models.EmailField(max_length=60,blank=True,null=True)
    nr_banco = models.IntegerField(blank=True,null=True)
    banco = models.CharField(max_length=40,blank=True,null=True)
    tp_conta = models.CharField(max_length=20,blank=True,null=True)
    agencia = models.CharField(max_length=15,blank=True,null=True)
    nr_conta = models.CharField(max_length=20,blank=True,verbose_name="Número da conta",null=True)
    status=models.CharField(max_length=25,blank=True,null=True)
    obs = models.CharField(max_length=90,blank=True,null=True)
    def __str__(self):
        return self.nm
    class Meta:
        verbose_name='1. Cadastro'
