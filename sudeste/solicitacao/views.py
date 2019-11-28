from django.shortcuts import render

def index(request):
    contexto = {'contexto':'contexto'}
    return render(request,'solicitacao/index.html',context={'contexto':contexto})