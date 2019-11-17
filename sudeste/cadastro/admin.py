from django.contrib import admin
from .models import identidadejuridica, cidade, estado, colaborador,cacamba ,historicocacamba,tipocacamba



class historicocacambaAdmin(admin.TabularInline):
    model = historicocacamba
    def get_extra(self, request, obj=None,**kwargs):
        extra = 1
        return extra

class cacambaAdmin(admin.ModelAdmin):
    list_display =('nrcacamba','tpCacamba','espCacamba','capCacamba','sttCacamba','tamCacamba','traCacamba','funCacamba','argCacamba','pinCacamba')
    inlines = [historicocacambaAdmin]
    view_on_site = True

class cadastroMain(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'bairro', 'fone1')


class identidadejuridicaAdmin(admin.ModelAdmin):
    list_display = ('nm', 'categoria', 'cidade', 'estado', 'contato', 'status')


admin.site.register(colaborador)
admin.site.register(identidadejuridica, identidadejuridicaAdmin)
admin.site.register(cacamba,cacambaAdmin)
admin.site.register(cidade)
admin.site.register(estado)
admin.site.register(tipocacamba)
