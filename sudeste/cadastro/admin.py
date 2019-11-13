from django.contrib import admin
from .models import cadastro_geral, cidade, estado, fornecedor


class smetal(admin.ModelAdmin):
    view_on_site = True


class cadastroMain(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'bairro', 'fone1')


class fornecedorAdmin(admin.ModelAdmin):
    list_display = ('nm_fornecedor', 'categoria', 'cidade', 'estado', 'comprador', 'status')


admin.site.register(cadastro_geral)
admin.site.register(fornecedor, fornecedorAdmin)
admin.site.register(cidade)
admin.site.register(estado)
