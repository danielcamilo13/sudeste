from django.contrib import admin
from datetime import datetime,date
from django.utils import timezone
from .models import pedidos, pedidosLista, pedidosFaturamento

def bulk_change(modelAdmin,request,queryset):
    queryset.update(faturado=True)
    queryset.update(dt_fat=timezone.now())
    
def bulk_rollback(modelAdmin,request,queryset):
    queryset.update(faturado=False)
    queryset.update(dt_fat=None)
  
bulk_change.short_description='Faturar serviços selecionados'
bulk_rollback.short_description='cancelar faturas dos serviços'
  
class pedidosAdmin(admin.ModelAdmin):
    list_display = ['fornecedor','status','tp_pedido','dt_saida','valor','total','status','faturado','finalizado']
    fieldsets = (('Dados do Fornecedor',{
                'fields':(('fornecedor'),
                ('tp_pedido','nr_pedido','qte'),
                'dt_saida','dt_entrada',
                ('valor','total'),
                'status',
                ('dt_fat','faturado'),
                'obs','finalizado')}),)
    view_on_site = True
    actions = [bulk_change,bulk_rollback]
    search_fields = ['pedido',]

class pedidosListaAdmin(admin.ModelAdmin):
    list_display = ['status','fornecedor','tp_pedido','dt_saida','finalizado']
    fieldsets = (('Dados do Pedido',{
                'fields':(('status','cacamba'),
                ('fornecedor'),
                ('tp_pedido','nr_pedido'),
                ('peso1','peso2'),
                ('dt_saida'),
                'obs',)}),)

class pedidosFaturamentoAdmin(admin.ModelAdmin):
    list_display=['fornecedor','dt_saida','peso1','peso2','finalizado']

admin.site.register(pedidos,pedidosAdmin)
admin.site.register(pedidosLista,pedidosListaAdmin)
admin.site.register(pedidosFaturamento,pedidosFaturamentoAdmin)