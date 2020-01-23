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
    select_opcoes = forms.ModelChoiceField(queryset=tipocacamba.objects.all(),required=False,label='Selecionar cacamba')
    data = forms.DateField(required=False,widget=forms.SelectDateWidget(empty_label=("Ano", "Mes", "Dia"),),)
    nrOS = forms.CharField(max_length=40,required=False,label='Ordem de Serviço')
    nmCliente = forms.CharField(max_length=30,label='Cliente')
    localizacao = forms.CharField(max_length=200,label='Localizacao')

class textoForm(forms.Form):
    campo = forms.CharField(label='Digite ',required=False)
    data = forms.DateField(required=False,widget=forms.SelectDateWidget(empty_label=("Ano", "Mes", "Dia"),),)
