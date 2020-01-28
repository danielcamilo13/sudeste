from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from cadastro.models import tipocacamba
from solicitacao.models import ordemServico
from .forms import pedidosForm,opcoesForm,textoForm,statusForm
import time
from django.utils import timezone
from datetime import datetime

def index(request):
    return render(request,'solicitacao/index.html',{})

def pedidos(request):
    return render(request,'solicitacao/pedidos.html',{})

def pedidosDetalhe(request):
    #neworder = get_object_or_404(orderInstance,pk=pk)
    neworder = ordemServico.objects.all()
    usr = request.user.pk
    ses = request.session
    print(usr)
    print(ses)
    if request.method=='POST':
        selecionado = request.POST['selecionar_opcoes']
        localizado=''
        dia = timezone.now
        if selecionado == 'cacamba':
            localizado ={'retorno':'retorno de cacamba'}
            nros = time.time()
            form = opcoesForm(initial={'nrOS':nros,'nmCliente':request.user,'dia':dia,'tpsolicitacao':'cacamba'})
            return render(request,'solicitacao/pedidos.html',{'localizado':localizado,'form':form})
        elif selecionado == 'retirar':
            form = textoForm(initial={'dia':dia,'tpsolicitacao':'retirar'})
            return render(request,'solicitacao/pedidos.html',{'localizado':localizado,'form':form})
        else:
            form = statusForm(initial={'dataInicio':dia,'dataFim':dia,'tpsolicitacao':'retirar'})
            return render(request,'solicitacao/pedidos.html',{'localizado':localizado,'form':form})
    else:
        form = {'chave vazio':'valor vazio'}
        return render(request,'solicitacao/pedidos.html',{'localizado':localizado,'form':form})

def confirmacao(request):
    if request.method=='POST':
        d = request.POST['dia_day']
        m = request.POST['dia_month']
        a = request.POST['dia_year']
        dia_join = str(a)+'/'+str(m)+'/'+str(d)
        dia_valor = datetime.strptime(dia_join,'%Y/%m/%d')
        if request.POST['tpsolicitacao']=='cacamba':
            os = request.POST['nrOS']
            cli = request.POST['nmCliente']
            loc = request.POST['localizacao']
            contexto={'os':os,'cli':cli,'loc':loc,'dia_valor':dia_valor}
            ordemServico.objects.create(nrOS=os,dtSaida=dia_valor,nmCliente=cli)
            ordemServico.save
        elif request.POST['tpsolicitacao']=='retirar':
            contexto = {'dia_valor':dia_valor}
        else:
            contexto = {'dia_valor':dia_valor}
    return render(request,'solicitacao/confirmacao.html',{'request':request,'contexto':contexto})

def opcoes(request):
    selecionado = ''; pedidos=''
    if 'select_opcoes' in request.POST:
        selecionado = request.POST['select_opcoes']
        if selecionado=='cacamba':
            pedidos = tipocacamba.objects.values('tpCacamba')
            pedidos = list(pedidos)
            pedidos+=[{'quantidade':'quantidade'}]
        elif selecionado=='retirar':
            pedidos = ({'tpCacamba':'valor1'},{'tpCacamba':'valor2'},{'tpCacamba':'valor3'})
        elif selecionado=='estado':
            pedidos = ({'tpCacamba':'estado1'},{'tpCacamba':'estado2'},{'tpCacamba':'estado3'})
    return render(request,'solicitacao/index.html',context={'pedidos':pedidos,'selecionado':selecionado})

def gravar(request):
    return HttpResponse('Gravado')
