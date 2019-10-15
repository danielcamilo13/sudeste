from django.contrib import admin
from .models import cadastro_geral,cidade,estado

class smetal(admin.ModelAdmin):
    view_on_site = True
    
class cadastroMain(admin.ModelAdmin):
    list_display =('nome','categoria','bairro','fone1')

admin.site.register(cadastro_geral)
admin.site.register(cidade)
admin.site.register(estado)
