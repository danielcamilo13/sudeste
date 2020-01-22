from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from cadastro.models import tipocacamba
from .forms import pedidosForm,opcoesForm,textoForm


def index(request):
    return render(request,'solicitacao/index.html',{})

def pedidos(request):
    return render(request,'solicitacao/pedidos.html',{})

def pedidosDetalhe(request):
    if request.method=='POST':
        selecionado = request.POST['selecionar_opcoes']
        localizado=''
        if selecionado == 'cacamba':
            localizado ={'retorno':'retorno de cacamba'}
            print('foi localizado {}'.format(localizado))
            opt = opcoesForm(request.POST)
            return render(request,'solicitacao/pedidos.html',{'localizado':localizado,'opt':opt})
        else:
            opt = textoForm(request.POST)
            return render(request,'solicitacao/pedidos.html',{'localizado':localizado,'opt':opt})

    else:
        opt = {'chave vazio':'valor vazio'}
        return render(request,'solicitacao/pedidos.html',{'localizado':localizado,'opt':opt})

def confirmacao(request):
    return render(request,'solicitacao/confirmacao.html',{'request':request})

#def pedidos(request):
#    if request.method == 'POST':
#        form = orderForm(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect('solicitacao/confirmacao.html')
#    else:
#        form = orderForm()
#    return render(request,'solicitacao/retorno.html',{'form':form})

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

def confirmacao(request):
    #retorno = request.POST['tpCacamba']
    for k,v in request.POST.getlist():
        print('valor do k e do v')
    retorno = str(request.META['QUERY_STRING'])

    return render(request,'solicitacao/confirmacao.html',{'retorno':retorno})

def gravar(request):
    return HttpResponse('Gravado')
