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

# from django.shortcuts import render
# from django.http import HttpResponse,HttpResponseRedirect
# from django.shortcuts import render
# from cadastro.reader_file import reading
# from .forms import UploadFileForm
# from django.conf import settings
# import datetime




# def index(request):
#     return HttpResponse('Retorno')
#
# def inputting(request):
#     resposta = 'a resposta é esta'
#     return render(request,'cadastro/inputting.html',{'pergunta':resposta})
#
# def review(request):
#     # print('Tratando a planilha')
#     # print('minha requisicao {}'.format(request.POST))
#     p1_files = {'arquivo':'arquivo'}
#     # if 'planilha' in request.POST:
#     #     p1 = request.POST['planilha']
#     #     p1_files = request.FILES[p1]
#     #     print('minha planilha {}'.format(pl))
#     #     print(pl_files.name)
#     #     print(pl_files.conent)
#     #     leitor = reading(pl_files)
#     return render(request,'cadastro/review.html',{'arquivo':p1_files})
#
# # Imaginary function to handle an uploaded file.
# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
#
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             planilha = request.POST['planilha']
#             handle_uploaded_file(request.FILES['planilha'])
#             return HttpResponseRedirect('cadastro/review.html')
#     else:
#         form = UploadFileForm()
#     return render(request, 'cadastro/inputting.html', {'form': form})
#
# def file_upload(request):
#     save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', request.FILES['file'])
#     path = default_storage.save(save_path, request.FILES['file'])
#     return default_storage.path(path)