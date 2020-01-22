from django import forms
from django.forms import widgets
from cadastro.models import tipocacamba

class pedidosForm(forms.Form):
    solicitar = 'Solicitar Cacamba'
    retirar = 'Retirar Cacamba'
    status = 'Status de Pedido'
    opcoes = (
        (solicitar,'Solicitar Cacamba'),
        (retirar,'Retirar Cacamba'),
        (status,'Status de Pedido'),
        )
    select_opcoes = forms.ChoiceField(choices=opcoes,label='Selecionar opções')

class opcoesForm(forms.Form):
    select_opcoes = forms.ModelChoiceField(queryset=tipocacamba.objects.all(),required=False,label='Selecionar opcoes')
    data = forms.DateField(required=False,widget=forms.SelectDateWidget(empty_label=("Ano", "Mes", "Dia"),),)

class textoForm(forms.Form):
    campo = forms.CharField(label='Digite ',required=False)
    data = forms.DateField(required=False,widget=forms.SelectDateWidget(empty_label=("Ano", "Mes", "Dia"),),)
