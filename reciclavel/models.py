from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cadastro.models import cadastro_geral    
from datetime import datetime
from django.contrib import admin

@python_2_unicode_compatible
class pedidos(models.Model):
    a = 'em andamento'
    b = 'pendente'
    c = 'rejeitado'
    d = 'finalizado'
    e = 'transporte'
    f = 'Solicitar retirada'
    g = 'Confirmar retirada'
    status_opt = (
    (a,'em andamento'),
    (b,'pendente'),
    (c,'rejeitado'),
    (d,'finalizado'),
    (e,'transporte'),
    (f, 'Solicitar retirada'),
    (g,'Confirmar retirada')
    )
    pole ='pole'
    rolon='rolon'
    muk = 'muk'
    tipos_cacamba = (
        (pole,'pole'),
        (rolon,'rolon'),
        (muk,'muk')
        )
    id = models.AutoField(primary_key=True)
    nr_pedido = models.CharField(max_length=10,blank=True,verbose_name='Nr Controle Pedido',null=True)
    tp_pedido = models.CharField(max_length=10,blank=True,verbose_name='Ordem',null=True)
    qte = models.IntegerField(blank=True,verbose_name='Quantidade',null=True,default=1)
    dt_saida = models.DateField(blank=True,verbose_name='Saída',null=True,default=datetime.now)
    dt_entrada = models.DateField(verbose_name='Entrada',blank=True,null=True)
    fornecedor = models.ForeignKey(cadastro_geral,on_delete=models.CASCADE,max_length=90,blank=True,null=True)
    valor = models.DecimalField(max_digits=8,decimal_places=2,blank=True,verbose_name='Valor',null=True,default=0)
    total = models.DecimalField(max_digits=8,decimal_places=2,blank=True,verbose_name='Total',null=True,default=0)
    status = models.CharField(max_length=18, choices=status_opt,null=True,verbose_name='Status',default='Solicitar retirada')
    cacamba = models.CharField(max_length=6,choices=tipos_cacamba,null=True,verbose_name='Tipos de Cacambas')
    peso1 = models.IntegerField(blank=True,verbose_name='Peso aproximado em KGs',null=True)
    peso2 = models.IntegerField(blank=True,verbose_name='Peso real',null=True)
    obs = models.CharField(max_length=90,blank=True,verbose_name='Observação',null=True)
    finalizado = models.BooleanField(blank=True,null=True)
    faturado = models.BooleanField(blank=False,default=False)
    dt_fat = models.DateField(blank=True,verbose_name='Data de Faturado',null=True)
    def __str__(self):
        return str(self.nr_pedido)
    class Meta:
        verbose_name = 'Pedidos - Sudeste'
        verbose_name_plural = 'Pedidos - Sudeste'
        
class pedidosLista(pedidos):
    class Meta:
        proxy = True
        verbose_name = 'retirada de material'
        verbose_name_plural = 'Retirada de Materiais'

class pedidosFaturamento(pedidos):
    class Meta:
        proxy=True
        verbose_name = 'Faturamento de Pedido'