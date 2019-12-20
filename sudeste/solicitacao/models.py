from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from datetime import datetime

@python_2_unicode_compatible
class ordemServico(models.Model):
    a = 'em andamento'
    b = 'pendente'
    c = 'rejeitado'
    d = 'finalizado'
    e = 'transporte'
    f = 'Solicitar retirada'
    g = 'Confirmar retirada'
    status_opt = (
        (a, 'em andamento'),
        (b, 'pendente'),
        (c, 'rejeitado'),
        (d, 'finalizado'),
        (e, 'transporte'),
        (f, 'Solicitar retirada'),
        (g, 'Confirmar retirada')
    )
    id = models.AutoField(primary_key=True)
    nrOS = models.CharField(max_length=20, blank=False, null=False, verbose_name='Ordem de Serviço')
    tpOS = models.CharField(max_length=10, blank=True, verbose_name='Tipo de Ordem', null=True)
    tpOperacao = models.CharField(max_length=20, blank=True, null=True, verbose_name='Tipo de Operação')
    dsOS = models.CharField(max_length=200, blank=True, null=True, verbose_name='Descrição')
    nmCliente = models.CharField(max_length=30, blank=False, null=True, verbose_name='Nome do Cliente',default='deixar nome usuario logado')
    nmColaborador = models.CharField(max_length=30, blank=True, null=True, verbose_name='colaborador',)
    status = models.CharField(max_length=18, choices=status_opt, null=True, verbose_name='Status',
                              default='Solicitar retirada')
    valor = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='Valor Total', null=True, default=0)
    dtSaida = models.DateField(blank=True, verbose_name='Saída', null=True, default=datetime.now)
    dtEntrada = models.DateField(verbose_name='Entrada', blank=True, null=True)
    pesoTotal = models.IntegerField(blank=True, verbose_name='Peso Total', null=True)
    qteTotal = models.IntegerField(blank=True, verbose_name='Quantidade Total', null=True, default=1)
    finalizado = models.BooleanField(blank=True, null=True)
    faturado = models.BooleanField(blank=False, default=False)
    dtFat = models.DateField(blank=True, verbose_name='Data de Faturado', null=True)
    def __str__(self):
        return str(self.nrOS)
    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de serviço'

@python_2_unicode_compatible
class ordemServicoItem(models.Model):
    id = models.AutoField(primary_key=True)
    nrItem = models.CharField(max_length=10, blank=True, verbose_name='Nr Controle Pedido', null=True)
    qte = models.IntegerField(blank=True, verbose_name='Quantidade', null=True, default=1)
    dtEntrada = models.DateField(verbose_name='Entrada', blank=True, null=True)
    ordemServico = models.ForeignKey(ordemServico, on_delete=models.CASCADE, max_length=90, blank=True, null=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='Valor', null=True, default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='Total', null=True, default=0)
    peso1 = models.IntegerField(blank=True, verbose_name='Peso aproximado em KGs', null=True)
    peso2 = models.IntegerField(blank=True, verbose_name='Peso real', null=True)
    obs = models.CharField(max_length=90, blank=True, verbose_name='Observação', null=True)
    def __str__(self):
        return str(self.nrItem)
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'




class solicitarRetirada(ordemServico):
    class Meta:
        proxy = True
        verbose_name = 'Solicitar retirada de material'
        verbose_name_plural = 'Retirada de Materiais'
#
#
# class pedidosFaturamento(pedidos):
#     class Meta:
#         proxy = True
#         verbose_name = 'Faturamento de Pedido'
