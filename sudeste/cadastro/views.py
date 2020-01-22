from django.shortcuts import render
from django.views.generic  import TemplateView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .reader_file import reading,spreadsheet_reader
import json

class Home(TemplateView):
    template_name = 'cadastro_home.html'


def upload(request):
    context ={}
    data = {}
    resultado = {}
    if request.method =='POST':
        upload_file = request.FILES['documento']
        data_file = {'name':upload_file.name,'size':upload_file.size}
        fs = FileSystemStorage()
        name = fs.save(upload_file.name,upload_file)
        leitor = reading(upload_file)
        context['url']=fs.url(name)
        resultado = spreadsheet_reader(upload_file)
    return render(request,'cadastro/upload.html',{'context':context,'resultado':resultado})
