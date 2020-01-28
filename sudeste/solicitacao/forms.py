from django import forms
from django.forms import widgets
from cadastro.models import tipocacamba
from .models import ordemServico
import time

#class pedidosForm(forms.Form):
class pedidosForm(forms.ModelForm):
    solicitar = 'Solicitar Cacamba'
    retirar = 'Retirar Cacamba'
    status = 'Status de Pedido'
    opcoes = (
        (solicitar,'Solicitar Cacamba'),
        (retirar,'Retirar Cacamba'),
        (status,'Status de Pedido'),
        )

class opcoesForm(forms.Form):
    nrOS = forms.CharField(max_length=40,required=False,label='Ordem de Serviço',initial='inicial')
    select_opcoes = forms.ModelChoiceField(queryset=tipocacamba.objects.all(),required=True,label='Selecionar cacamba',help_text='polen= 1 tonelada; muk=800 kgs; rolon:300 kgs')
    tpsolicitacao = forms.CharField(label='Tipo de solicitacao')
    qteCacamba=forms.IntegerField(required=False,label='Total',help_text='Total de cacambas para retirar o material')
    dia = forms.DateField(label='Melhor dia para locar cacamba:',required=False,widget=forms.SelectDateWidget(empty_label=("Ano", "Mes", "Dia"),),)
    nmCliente = forms.CharField(max_length=30,label='Cliente',required=False)
    localizacao = forms.CharField(max_length=200,label='Localizacao',required=False)
    def clean_nros(self):
        os = self.cleaned_data['nrOS']
        return os
    #class Meta:
    #    model = ordemServico

class textoForm(forms.Form):
    tpsolicitacao = forms.CharField(label='Tipo de solicitacao')
    dia = forms.DateField(required=False,widget=forms.SelectDateWidget(empty_label=("Ano", "Mes", "Dia"),),)

class statusForm(forms.Form):
    tpsolicitacao = forms.CharField(label='Tipo de solicitacao')
    dataInicio = forms.DateField(required=False,widget=forms.SelectDateWidget(empty_label=("Ano", "Mes", "Dia"),),)
    dataFim = forms.DateField(required=False,widget=forms.SelectDateWidget(empty_label=("Ano", "Mes", "Dia"),),)
