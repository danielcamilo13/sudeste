from django.contrib import admin
from .models import ordemServico,ordemServicoItem,solicitarRetirada

class ordemServicoItemAdmin(admin.TabularInline):
    model = ordemServicoItem
    def get_extra(self, request, obj=None,**kwargs):
        extra = 1
        return extra

class ordemServicoAdmin(admin.ModelAdmin):
    list_display = ('nrOS','tpOS','nmCliente','status','valor','dtSaida','dtEntrada','finalizado','faturado','nmColaborador')
    search_fields = ('nrOS','nmCliente')
    list_filter = ('dtSaida','nmCliente','nmColaborador')
    fieldsets = (
        (
            'Dados do Fornecedor',{
                'fields':(
                    ('nrOS','tpOS','tpOperacao','status'),
                    'dsOS',
                    ('nmCliente','nmColaborador'),
                    ('dtSaida','dtEntrada'),
                    ('pesoTotal','qteTotal','valor'),
                )
            }
        ),(
            'Faturamento',{
                'fields':(
                    ('faturado', 'dtFat', 'finalizado'),
        )
        }
        )
    )
    inlines = [ordemServicoItemAdmin]
    view_on_site = True

class solicitarRetiradaAdmin(admin.ModelAdmin):
    list_display = ('nrOS','tpOS','nmCliente','status','valor','dtSaida','dtEntrada','finalizado','faturado','nmColaborador')
    search_fields = ('nrOS','nmCliente')
    list_filter = ('dtSaida','nmCliente','nmColaborador')
    fieldsets = (
        (
            'Dados do Fornecedor',{
                'fields':(
                    ('nrOS','tpOS','tpOperacao','status'),
                    'dsOS',
                    ('nmCliente','nmColaborador'),
                    ('dtSaida','dtEntrada'),
                    ('pesoTotal','qteTotal','valor'),
                )
            }
        ),(
            'Faturamento',{
                'fields':(
                    ('faturado', 'dtFat', 'finalizado'),
        )
        }
        )
    )
    inlines = [ordemServicoItemAdmin]
    view_on_site = True

admin.site.register(ordemServico,ordemServicoAdmin)
admin.site.register(solicitarRetirada,solicitarRetiradaAdmin)